from pathlib import Path

from bs4 import BeautifulSoup


def main():
    html_file = Path(__file__).parent / "home.html"

    with html_file.open("r", encoding="utf-8") as file:
        content = file.read()

    soup = BeautifulSoup(content, "lxml")
    course_cards = soup.select(".course")

    for course in course_cards:
        course_name = course.find("h2").get_text(strip=True)
        course_price = course.find("a").get_text(" ", strip=True).split()[-1]
        print(f"{course_name} costs {course_price}")


if __name__ == "__main__":
    main()
