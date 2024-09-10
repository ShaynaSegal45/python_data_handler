def filter_by_industry(candidates: list, industry: str) -> list:
    filtered_candidates = []
    for candidate in candidates:
        for job in candidate.get('experience', []):
            if job.get('company_details') and 'industry' in job['company_details']:
                job_industry = job['company_details']['industry']
                if industry in job_industry:
                    filtered_candidates.append(candidate)
                    break
    return filtered_candidates

def filter_by_skills(candidates: list, required_skills: list) -> list:
    return [
        candidate for candidate in candidates 
        if all(skill in candidate.get('extracted_skills', []) for skill in required_skills)
    ]

def total_years_experience(experience: list) -> float:
    total_months = sum([job.get('duration_in_month', 0) for job in experience])
    return total_months / 12

def filter_by_experience_years(candidates: list, min_years: float) -> list:
    return [
        candidate for candidate in candidates
        if total_years_experience(candidate.get('experience', [])) >= min_years
    ]
