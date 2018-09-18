from pyramid.view import view_config
from pyramid.request import Request
from pyramid.httpexceptions import HTTPNotFound


fake_db = {
    'company/history': {
        'page_title': 'Company history',
        'page_details': 'Details about company history...',
    },
    'company/employees': {
        'page_title': 'Our team',
        'page_details': 'Details about company employees ...',
    },
}


@view_config(route_name='cms_page',
             renderer='pypi:templates/cms/page.pt')
def cms_page(request: Request):
    subpath = request.matchdict.get('subpath')
    suburl = '/'.join(subpath)  # join iterable subpath to string

    page = fake_db.get(suburl)
    if not page:
        raise HTTPNotFound()

    return page

