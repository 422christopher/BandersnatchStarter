from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """
    This class manages the monster database. It populates monsters,
    resets the monster table, counts the monsters on the table,
    and creates a dataframe of the monster table that can be
    rendered as an HTML table on the website.
    """
    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Database"]

    def __init__(self, collection: str):
        self.collection = self.database[collection]

    # Inserts a specified number of documents into the collection.
    def seed(self, amount: int):
        self.monsters = [Monster().to_dict() for i in range(amount)]
        return self.collection.insert_many(self.monsters)

    # Deletes all documents from the collection.
    def reset(self):
        return self.collection.delete_many({})

    # Returns the number of documents in the collection.
    def count(self) -> int:
        return self.collection.count_documents({})

    # Returns a DataFrame containing all documents in the collection
    def dataframe(self) -> DataFrame:
        return DataFrame(list(self.collection.find({})))

    # Returns an HTML table representation of the DataFrame, or None if the collection is empty.
    def html_table(self) -> str:
        if self.count() > 0:
            return self.dataframe().to_html()
        else:
            return "The collection is empty."
