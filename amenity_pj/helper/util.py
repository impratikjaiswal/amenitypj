from amenity_pj.helper.constants import Const


class Util:

    @classmethod
    def get_github_url(cls, github_repo=None, github_pages=True):
        default_url = Const.GITHUB_PAGES if github_pages else Const.GITHUB_REPO
        return '/'.join(filter(None, [default_url, github_repo]))
