project_obj = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}

result = list(set(project_obj.values()))
result.sort()
print(result)