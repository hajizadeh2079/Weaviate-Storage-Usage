import random
import weaviate
from testsamples import *

def create_schema():
    schema = {
        "classes": [
            {
                "class": "Person",
                "description": "A person",
                "properties": [
                    {
                        "name": "name",
                        "dataType": ["string"],
                        "description": "The name of the person"
                    },
                    {
                        "name": "age",
                        "dataType": ["int"],
                        "description": "The age of the person"
                    },
                    {
                        "name": "address",
                        "dataType": ["string"],
                        "description": "The address of the person"
                    }
                ]
            },
            {
                "class": "Organization",
                "description": "An organization",
                "properties": [
                    {
                        "name": "name",
                        "dataType": ["string"],
                        "description": "The name of the organization"
                    }
                ]
            }
        ]
    }
    try:
        client.schema.create(schema)
        print("Schema created successfully")
    except Exception as e:
        print(f"Error creating schema: {e}")

def insert_data():
    client.batch.configure(batch_size=10000)
    for _ in range(100):
        with client.batch as batch:
            for _ in range(10000):
                name = random.choice(sample_names)
                city = random.choice(sample_cities)
                country = random.choice(sample_countries)
                street = random.choice(sample_streets)
                house_number = random.randint(1, 99)
                age = random.randint(18, 90)
                address = f'{street} {house_number}, {city}, {country}'
                properties = {
                    "name": name,
                    "age": age,
                    "address": address
                }
                batch.add_data_object(
                    data_object=properties,
                    class_name="Person"
                )
        with client.batch as batch:
            for _ in range(10000):
                name = random.choice(sample_organization_names)
                properties = {
                    "name": name,
                }
                batch.add_data_object(
                    data_object=properties,
                    class_name="Organization"
                )

if __name__ == "__main__":
    client = weaviate.Client("http://localhost:8080")
    create_schema()
    insert_data()
