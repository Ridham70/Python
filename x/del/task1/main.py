import json, unittest, datetime

with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1 (jsonObject):
    location_parts = jsonObject['location'].split('/')
    return {
        "deviceID": jsonObject['deviceID'],
        'deviceType': jsonObject['deviceType'],
        'timestamp': jsonObject['timestamp'],
        'location': {
            'country': location_parts[0],
            'city': location_parts[1],
            'area': location_parts[2],
            'factory': location_parts[3],
            'section': location_parts[4]
        },
        'data': {
            'status': jsonObject['operationStatus'],
            'temperature': jsonObject['temp']
        }
    }


def convertFromFormat2 (jsonObject):
    timestamp_str = jsonObject['timestamp']
    dt = datetime.datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    timestamp_millis = int(dt.timestamp() * 1000)
    location = {
        'country': jsonObject['country'],
        'city': jsonObject['city'],
        'area': jsonObject['area'],
        'factory': jsonObject['factory'],
        'section': jsonObject['section']
    }
    device_info = jsonObject['device']
    return {
        'deviceID': device_info['id'],
        'deviceType': device_info['type'],
        'timestamp': timestamp_millis,
        'location': location,
        'data': jsonObject['data']
    }


def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()

