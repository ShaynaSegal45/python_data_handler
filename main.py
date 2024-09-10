import logging
from db import insert_into_mongodb
from filters import filter_by_industry, filter_by_skills, filter_by_experience_years
from utils import get_candidate_data

URL = 'https://hs-recruiting-test-resume-data.s3.amazonaws.com/allcands-full-api_hub_b1f6-acde48001122.json'
COLLECTION_NAME = 'filtered_candidates'


def main():
    candidates = get_candidate_data(URL)

    if not candidates:
        logging.error("No candidate data available to process.")
        return

#test example should insert 1 candidate named Clark L Kent
    industry = 'Real Estate industry'
    required_skills = ['Wax wise', 'Wax']
    min_years = 1

    candidates = filter_by_industry(candidates, industry)
    candidates = filter_by_skills(candidates, required_skills)
    candidates = filter_by_experience_years(candidates, min_years)

   # insert_into_mongodb(COLLECTION_NAME, candidates)
    
#test example insert 1 candidate Bruce Wayne
    industry = 'Education Management industry'
    required_skills = ['HHH']
    min_years = 3

    candidates = get_candidate_data(URL)
    candidates = filter_by_industry(candidates, industry)
    candidates = filter_by_skills(candidates, required_skills)
    candidates = filter_by_experience_years(candidates, min_years)

    insert_into_mongodb(COLLECTION_NAME, candidates)

if __name__ == "__main__":
    main()
