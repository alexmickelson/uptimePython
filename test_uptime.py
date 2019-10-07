from uptimeCheck import checkstate
from uptimeCheck import getStateChange
import unittest
import unittest.mock as mock
from socket import timeout


class CheckStateTest(unittest.TestCase):

    @mock.patch('uptimeCheck.urllib.request')
    def test_UpState(self, mock_request):
        mock_request.urlopen.return_value = "doesn'tMatter"
        result = checkstate("somedummysite.edu")
        self.assertEqual("up", result)

    @mock.patch('uptimeCheck.urllib.request')
    def test_DownState(self, mock_request):
        error = timeout("timeout")
        error.reason = timeout("timeout")
        mock_request.urlopen.side_effect = error
        result = checkstate(
            "somedummysitedsafsdfasdfasdfasdfasdfasdfadsfasdfasdfasdfedu")
        self.assertEqual("down", result)

    @mock.patch('uptimeCheck.datetime')
    def test_doesNothingIfNoStateChange(self, mock_datetime):
        mock_datetime.now.return_value = 'nowTime'
        returnValue = getStateChange("one", "one")
        self.assertIsNone(returnValue)

    @mock.patch('uptimeCheck.datetime')
    def test_CorrectActionOnStateChange(self, mock_datetime):
        mock_datetime.now.return_value = 'nowTime'
        returnValue = getStateChange("one", "two")
        self.assertEqual("New State: one Time: nowTime", returnValue)


if __name__ == "__main__":
    unittest.main()
