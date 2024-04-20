import json

from classes import Day, Event, Instructor


def scrape_dance_atelier(soup):
    if soup:
        scrape_data = []

        for day in soup.find_all(class_='content-box schedule-box'):
            day_of_the_week_element = day.find('h2')
            if day_of_the_week_element:
                day_of_the_week = day_of_the_week_element.text.strip()
                current_day = Day(day_of_the_week)
                tbody = day.find('tbody')
                if tbody:
                    for hour in tbody.find_all('tr'):
                        time = hour.find('td').text.strip()
                        event_cells = hour.find_all(
                            class_='event-schedule-cell')
                        for event in event_cells:
                            name = event.find('h4').text.strip()
                            instructor_name_element = event.find('h5')
                            instructor_name = instructor_name_element.text.strip(
                            ) if instructor_name_element else ""
                            instructor_link_element = event.find('a')
                            instructor_link = instructor_link_element['href'] if instructor_link_element else ""
                            instructor = Instructor(
                                instructor_name, instructor_link)
                            level_element = event.find('span')
                            level = level_element.text.strip() if level_element else ""
                            current_event = Event(
                                time, name, instructor, level)
                            current_day.add_event(current_event)

                scrape_data.append(current_day)

        return scrape_data
