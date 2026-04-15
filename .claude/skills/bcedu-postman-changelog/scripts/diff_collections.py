import json

old = json.loads(open('/tmp/old_collection.json').read() or '{}')
new = json.loads(open('/tmp/new_collection.json').read())

# Collection info
print("COLLECTION_NAME:", new['info']['name'])

# Variables
old_vars = {v['key']: v['value'] for v in old.get('variable', [])}
new_vars = {v['key']: v['value'] for v in new.get('variable', [])}
print("VARS_ADDED:", json.dumps({k: new_vars[k] for k in new_vars if k not in old_vars}))
print("VARS_REMOVED:", json.dumps({k: old_vars[k] for k in old_vars if k not in new_vars}))
print("VARS_MODIFIED:", json.dumps({k: [old_vars[k], new_vars[k]] for k in old_vars if k in new_vars and old_vars[k] != new_vars[k]}))

# Auth
old_auth = json.dumps(old.get('auth', {}), sort_keys=True)
new_auth = json.dumps(new.get('auth', {}), sort_keys=True)
print("AUTH_CHANGED:", "true" if old_auth != new_auth else "false")
if old_auth != new_auth:
    print("AUTH_OLD:", old_auth)
    print("AUTH_NEW:", new_auth)

# Collection-level events
def event_map(obj):
    return {e['listen']: json.dumps(e.get('script', {}).get('exec', []), sort_keys=True) for e in obj.get('event', [])}

old_ev, new_ev = event_map(old), event_map(new)
changed_events = [k for k in set(list(old_ev) + list(new_ev)) if old_ev.get(k) != new_ev.get(k)]
print("COLLECTION_EVENTS_CHANGED:", json.dumps(changed_events))

# Folders and requests
old_folders = {f['name']: f for f in old.get('item', [])}
new_folders = {f['name']: f for f in new.get('item', [])}
print("FOLDERS_ADDED:", json.dumps([n for n in new_folders if n not in old_folders]))
print("FOLDERS_REMOVED:", json.dumps([n for n in old_folders if n not in new_folders]))

for fname in sorted(set(list(old_folders) + list(new_folders))):
    if fname not in old_folders or fname not in new_folders:
        continue
    old_reqs = {r['name']: r for r in old_folders[fname].get('item', [])}
    new_reqs = {r['name']: r for r in new_folders[fname].get('item', [])}
    modified = {}
    for name in set(old_reqs) & set(new_reqs):
        if json.dumps(old_reqs[name], sort_keys=True) == json.dumps(new_reqs[name], sort_keys=True):
            continue
        changes = []
        or_, nr_ = old_reqs[name]['request'], new_reqs[name]['request']
        if or_.get('method') != nr_.get('method'):
            changes.append(f"method: {or_.get('method')} → {nr_.get('method')}")
        if json.dumps(or_.get('url'), sort_keys=True) != json.dumps(nr_.get('url'), sort_keys=True):
            changes.append('url')
        if json.dumps(or_.get('header'), sort_keys=True) != json.dumps(nr_.get('header'), sort_keys=True):
            changes.append('headers')
        ob, nb = or_.get('body', {}), nr_.get('body', {})
        if ob.get('mode') != nb.get('mode'):
            changes.append(f"body mode: {ob.get('mode')} → {nb.get('mode')}")
        elif ob.get('mode') == 'graphql':
            og, ng = ob.get('graphql', {}), nb.get('graphql', {})
            if og.get('query') != ng.get('query'):
                changes.append('graphql query')
            if og.get('variables') != ng.get('variables'):
                changes.append('graphql variables')
        elif ob.get('mode') == 'raw' and ob.get('raw') != nb.get('raw'):
            changes.append('raw body')
        oe = event_map(old_reqs[name])
        ne = event_map(new_reqs[name])
        for t in set(list(oe) + list(ne)):
            if oe.get(t) != ne.get(t):
                changes.append(f'test scripts ({t})')
        if changes:
            modified[name] = changes
    safe = fname.replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '')
    print(f"FOLDER__{safe}__ADDED:", json.dumps([n for n in new_reqs if n not in old_reqs]))
    print(f"FOLDER__{safe}__REMOVED:", json.dumps([n for n in old_reqs if n not in new_reqs]))
    print(f"FOLDER__{safe}__MODIFIED:", json.dumps(modified))
