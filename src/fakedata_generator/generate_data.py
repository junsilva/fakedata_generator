import csv
import argparse
import random
from faker import Faker

# Initialize Faker
fake = Faker()


def generate_data(num_rows, max_skills):
    # Create a set to store unique skills
    unique_skills = set()

    # Generate a pool of unique skills
    while len(unique_skills) < 100:  # Generate at least 20 unique skills
        unique_skills.add(fake.word().capitalize())

    # Convert the set to a list for sampling
    skills_list = list(unique_skills)

    # Create job entries
    jobs = []
    for i in range(1, num_rows + 1):
        title = fake.job()
        num_required_skills = random.randint(1, max_skills)
        required_skills = random.sample(skills_list, num_required_skills + 1)
        jobs.append(
            {"id": i, "title": title, "required_skills": ", ".join(required_skills)}
        )

    # Write to CSV
    with open(f"jobs_{num_rows}.csv", "w", newline="") as csvfile:
        fieldnames = ["id", "title", "required_skills"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for job in jobs:
            writer.writerow(job)

    print(f"Generated {num_rows} job entries in 'jobs_{num_rows}.csv'.")

    # Create job entries
    jobseekers = []
    for i in range(1, num_rows + 1):
        name = fake.name()
        num_skills = random.randint(1, max_skills)
        skills = random.sample(skills_list, num_skills + 1)
        jobseekers.append({"id": i, "name": name, "skills": ", ".join(skills)})

    # Write to CSV
    with open(f"jobseekers_{num_rows}.csv", "w", newline="") as csvfile:
        fieldnames = ["id", "name", "skills"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for seeker in jobseekers:
            writer.writerow(seeker)

    print(f"Generated {num_rows} job seeker entries in 'jobseekers_{num_rows}.csv'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a jobs CSV file.")
    parser.add_argument("num_rows", type=int, help="Number of job rows to create.")
    parser.add_argument("max_skills", type=int, help="Maximum number of skills per job.")

    args = parser.parse_args()
    generate_data(args.num_rows, args.max_skills)
