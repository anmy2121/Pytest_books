import collections
from src.services.user_fetcher_service import UserFetcherService
from src.services.user_service import UserService

def test_list_user_ids(monkeypatch):

    def mock_get_users(*args):
        return [
            {'id': '1', 'email': 'lolo@gmail.com'},
            {'id': '2', 'email': 'lala@gmail.com'},

        ]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
    ids = user_service.list_users()

    assert ids == [{'id': '1', 'email': 'lolo@gmail.com'}, {'id': '2', 'email': 'lala@gmail.com'}]



