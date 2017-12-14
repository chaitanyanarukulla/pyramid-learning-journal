# pyramid-learning-journal


**Authors:**
Chaitanya.Narukulla (chaitanya.narukulla@gmail.com)

**Deployed Site**https://shrieking-skull-73949.herokuapp.com/

Building web-page to post my blogs using the [Pyramid FrameWork](https://trypyramid.com/),
[cookiecutter-pypackage](https://cookiecutter.readthedocs.io/en/latest/readme.html) and the [Clean-blog Boot Strap](https://startbootstrap.com/template-overviews/clean-blog/)

## Routes:

"/"- the home page and a listing of all Blogs

"/new-entry" - to create a new Blog

"/post/{id:\d+}" - check old post of Blogs

"/edit-entry/{id:\d+}/edit" - for editing Old Blog post



home page that shows a list of journal entries with just the title and date created.
The second page will be a detail page that shows a single entry. The title, text and created date should be displayed on this page.
The third page will  be an HTML form page will will use to create a new entry. The title and text of the entry should be inputs in this form, empty at first.
The fourth will   be an HTML form page you will use to edit an existing entry. The title and text of the entry will be inputs in this form




## Set Up and Installation:

- Clone this repository to your local machine.

```https://github.com/chaitanyanarukulla/pyramid-learning-journal```

Once downloaded, cd into the learning_journal directory.

Begin a new virtual environment with Python 3 and activate it.

pip install setup.py  this package as well as the testing set of extras into your virtual environment.

$ initialize_db development.ini to initialize the database, populating with random models.

$ pserve development.ini --reload to serve the application on http://localhost:6543

To Test

If you have the testing extras installed, testing is simple. If you're in the same directory as setup.py type the following:

$ py.test learning_journal

```

Test coverage for step 2


```
Step 1 test Coverage:
```---------- coverage: platform darwin, python 3.6.3-final-0 -----
Name                                 Stmts   Miss  Cover   Missing
------------------------------------------------------------------
learning_journal/Data/entry.py           1      0   100%
learning_journal/models/meta.py          5      0   100%
learning_journal/models/mymodel.py       8      0   100%
learning_journal/tests.py               46      0   100%
learning_journal/views/default.py       16      0   100%
learning_journal/views/notfound.py       4      2    50%   8-9
------------------------------------------------------------------
TOTAL                                   80      2    98%```
```
```
Step 2 TEST:COVERAGE

---------- coverage: platform darwin, python 3.6.3-final-0 -------
Name                                 Stmts   Miss  Cover   Missing
------------------------------------------------------------------
learning_journal/Data/__init__.py        0      0   100%
learning_journal/Data/entry.py           1      0   100%
learning_journal/routes.py               6      0   100%
learning_journal/views/default.py       22      1    95%   34
learning_journal/views/notfound.py       4      2    50%   
------------------------------------------------------------------
TOTAL                                   33      3    91%
```

```
Step 3 TEST:COVERAGE
Name                                  Stmts   Miss  Cover   
-------------------------------------------------------------------
learning_journal/Data/__init__.py         0      0   100%
learning_journal/Data/entry.py            1      0   100%
learning_journal/models/__init__.py      24      3    88%   
learning_journal/models/meta.py           5      0   100%
learning_journal/models/mymodel.py       11      0   100%
learning_journal/routes.py                6      0   100%
learning_journal/views/default.py        21      6    71%   34,
learning_journal/views/notfound.py        4      2    50%   8-9
-------------------------------------------------------------------
TOTAL                                    72     11    95%
```

Resources used:

This project was modeled using this repos and some of the code was used from this resources :

youtube:https://www.youtube.com/playlist?list=PLVngfM2hsbi-Uo2jDso-K06VScDC1ucMy

https://github.com/markreynoso/pyramid-learning-journal


https://github.com/ztaylor2/pyramid-learning-journalion on http://localhost:6543

https://github.com/codefellows/expense_tracker_401d7

