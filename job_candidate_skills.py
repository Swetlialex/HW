skill_required = {'Python', 'Django','SQL','Git'}
skill_candidate = {'Python', 'Flask','Git','JavaScript'}
matched_skills = skill_required.intersection(skill_candidate)
print('Matched Skills: ', matched_skills)
missing_skills = skill_required.difference(skill_candidate)
print('Missing Skills: ', missing_skills)
extra_skills = skill_candidate.difference(skill_required)
print('Extra skills: ', extra_skills)



