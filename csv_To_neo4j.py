from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "your URI"
AUTH = ("neo4j", "your password")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()