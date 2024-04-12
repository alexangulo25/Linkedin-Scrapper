import requests
from bs4 import BeautifulSoup

def fetch_job_posts(keyword, location):
    try:
        # LinkedIn job search URL
        url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location={location}"
        
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            print(soup)
            # Find all list items with class 'tw-link-column-item'
            job_elements = soup.find_all('li', class_='tw-link-column-item')
            
            # Extract links from each list item
            job_links = []
            for job_element in job_elements:
                link = job_element.find('a', class_='link tw-linkster-link')
                if link:
                    job_links.append(link['href'])
            
            return job_links
        else:
            print("Failed to fetch job posts. Status code:", response.status_code)
            return []
    except Exception as e:
        print("An error occurred:", e)
        return []

# Example usage
if __name__ == "__main__":
    keyword = "Python Developer"  # Specify the keyword for job search
    location = "Colombia"         # Specify the location for job search
    
    job_links = fetch_job_posts(keyword, location)
    
    if job_links:
        for idx, link in enumerate(job_links, start=1):
            print(f"Job {idx}: {link}")
    else:
        print("No job links found.")
