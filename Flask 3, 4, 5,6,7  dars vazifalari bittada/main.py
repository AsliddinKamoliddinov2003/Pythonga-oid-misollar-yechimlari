from config import app

from Category_views import *
from errors_views import *
from News_vews import *
from admin_news_view import *



if __name__ == "__main__":
    from Context import *
    app.run(debug=True)