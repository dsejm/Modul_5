import json
class Model:
    title = "title"
    text = "text"
    author = "author"


    def save(self):
        with open(f"model_attributes_{self.author}.json", "w") as file:
            list_atr = list(filter(lambda x: not x.startswith('_'), dir(Model)))
            list_atr.remove("save")
            list_atr = list_atr[::-1]
            list_value = []
            list_value.append(self.title)
            list_value.append(self.text)
            list_value.append(self.author)
            data = dict(zip(list_atr, list_value))
            json.dump(data, file)
            print("Data save!")
