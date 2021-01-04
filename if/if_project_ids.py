project_ids = ['01234', '24253']

projekt_id = '02135'

if projekt_id not in project_ids:
    project_ids.append(projekt_id)

print(project_ids)

pro_ids = {
    '01': 'open',
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}

if pro_ids.get('02') == 'new':
    pro_ids['02'] = 'open'

print(pro_ids)