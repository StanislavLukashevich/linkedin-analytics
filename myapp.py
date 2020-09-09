import os
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import app

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app_dash = dash.Dash(__name__, server=app, external_stylesheets=external_stylesheets, url_base_pathname='/dash/')
app_dash.layout = html.Div([html.H1('Hi there, I am app1 for dashboards')])


def runScraping(username_string, password_string, link_username):
    # GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    # CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    # chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', 'chromedriver')
    #
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = chrome_bin
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--headless")
    #
    # browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    browser = webdriver.Chrome('/usr/local/bin/chromedriver')

    # open the LinkedIn login page and login under a specified account:
    browser.get('https://www.linkedin.com/login')

    # sleep time for 15 secs

    # enter the specified information to login to LinkedIn:
    elementID = browser.find_element_by_id('username')
    elementID.send_keys(username_string)
    elementID = browser.find_element_by_id('password')
    elementID.send_keys(password_string)
    btn = browser.find_element_by_class_name('btn__primary--large')
    btn.submit()

    recent_activity_link = "https://www.linkedin.com/in/" + link_username + "/detail/recent-activity/shares/"
    browser.get(recent_activity_link)

    like = browser.find_element_by_class_name('social-details-social-counts__reactions-count')
    if like:
        return 'YES' + str(like)
    else:
        return 'NOT FOUND'
    # number_of_scrolls = (int(number_of_posts) // 5)  # 5 is LinkedIn's number of posts per scroll

    # # we need a loop because we have a particular number of scrolls...
    # likes = []
    # comments = []
    # views = []
    #
    # SCROLL_PAUSE_TIME = 5
    #
    # # Get scroll height
    # last_height = browser.execute_script("return document.documentElement.scrollHeight")
    #
    # for scroll in range(number_of_scrolls):
    #     # Scroll down to bottom
    #     browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    #     # Wait to load page
    #     time.sleep(SCROLL_PAUSE_TIME)
    #     # Calculate new scroll height and compare with last scroll height
    #     new_height = browser.execute_script("return document.documentElement.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height
    #
    # # query the contents (returns service reponse object with web contents, url headers, status and other):
    # src = browser.page_source
    # # beautiful soup instance:
    # soup = BeautifulSoup(src, features="lxml")  # lxml
    #
    # # find LIKES on LinkedIn
    # # look for "span" tags that have the specific following attribute (click 'inspect' on the L-in page)
    # # need to convert the list of bs4 tags into strings and then extract
    # # find these specific tags ("<stuff>") in the soup contents:
    #
    # likes_bs4tags = soup.find_all("span", attrs={"class": "v-align-middle social-details-social-counts__reactions-count"})
    #
    # # converts a list of 1 string to int, appends to likes list
    # for tag in likes_bs4tags:
    #     strtag = str(tag)
    #     # the first argument in findall (below) is a regular expression (accounts for commas in the number)
    #     list_of_matches = re.findall('[,0-9]+', strtag)
    #     # converts the last element (string) in the list to int, appends to likes list
    #     last_string = list_of_matches.pop()
    #     without_comma = last_string.replace(',', '')
    #     likes_int = int(without_comma)
    #     likes.append(likes_int)
    #     print(likes)
    #
    # return str(likes)

    # # find COMMENTS on LinkedIn
    # # same concept here
    # comments_bs4tags = soup.find_all("li", attrs={
    #     "class": "social-details-social-counts__item social-details-social-counts__comments"})
    # for tag in comments_bs4tags:
    #     strtag = str(tag)
    #     list_of_matches = re.findall('[,0-9]+', strtag)
    #     last_string = list_of_matches.pop()
    #     without_comma = last_string.replace(',', '')
    #     comments_int = int(without_comma)
    #     comments.append(comments_int)
    #
    # # find VIEWS on LinkedIn
    # # same concept here
    # views_bs4tags = soup.find_all("span", attrs={"class": "icon-and-text-container t-14 t-black--light t-normal"})
    # for tag in views_bs4tags:
    #     strtag = str(tag)
    #     list_of_matches = re.findall('[,0-9]+', strtag)
    #     last_string = list_of_matches.pop()
    #     without_comma = last_string.replace(',', '')
    #     views_int = int(without_comma)
    #     views.append(views_int)
    #
    # likes.reverse()
    # comments.reverse()
    # views.reverse()
    #
    # # Convert lists into pandas DataFrames
    # likes_df = pd.DataFrame(likes, columns=['Likes'])
    # comments_df = pd.DataFrame(comments, columns=['Comments'])
    # views_df = pd.DataFrame(views, columns=['Views'])
    #
    # # Get rid of the outliers
    # #   remove data points if further than 3 standard deviations away...
    # likes_df_no_outliers = likes_df[np.abs(likes_df - likes_df.median()) <= (3 * likes_df.std())]
    # comments_df_no_outliers = comments_df[np.abs(comments_df - comments_df.median()) <= (3 * comments_df.std())]
    # views_df_no_outliers = views_df[np.abs(views_df - views_df.median()) <= (3 * views_df.std())]
    # #   replace NaN values (deleted outliers) with the median values
    # likes_df_no_outliers['Likes'].fillna((likes_df_no_outliers['Likes'].median()), inplace=True)
    # comments_df_no_outliers['Comments'].fillna((comments_df_no_outliers['Comments'].median()), inplace=True)
    # views_df_no_outliers['Views'].fillna((views_df_no_outliers['Views'].median()), inplace=True)
    #
    # # # Need trend lines and slopes for analysis  & Visualize
    # # print('**************************')
    # # print('********* LIKES **********')
    # # print('**************************')
    # # coefficients_likes, residuals_likes, _, _, _ = np.polyfit(range(len(likes_df_no_outliers)), likes_df_no_outliers, 1,
    # #                                                           full=True)
    # # mse_likes = (residuals_likes[0]) / (len(likes_df_no_outliers))
    # # nrmse_likes = (np.sqrt(mse_likes)) / (likes_df_no_outliers.max() - likes_df_no_outliers.min())
    # # slope_likes = coefficients_likes[0]
    # # print('Slope: ' + str(slope_likes))
    # # print('NRMSE Error: ' + str(nrmse_likes))
    # # plt.plot(likes_df_no_outliers)
    # # plt.plot([slope_likes * x + coefficients_likes[1] for x in range(len(likes_df_no_outliers))])
    # #
    # # plt.title('Linkedin Post Likes for ' + link_username)
    # # plt.xlabel('Posts')
    # # plt.ylabel('Likes')
    # # plt.savefig(link_username + '-linkedin-likes-last-' + str(number_of_posts) + '-posts-GRAPH.png', dpi=600)
    # # plt.show()
    # # plt.clf()
    # #
    # # print('**************************')
    # # print('******* COMMENTS *********')
    # # print('**************************')
    # # coefficients_comments, residuals_comments, _, _, _ = np.polyfit(range(len(comments_df_no_outliers)),
    # #                                                                 comments_df_no_outliers, 1, full=True)
    # # mse_comments = (residuals_comments[0]) / (len(comments_df_no_outliers))
    # # nrmse_comments = (np.sqrt(mse_comments)) / (comments_df_no_outliers.max() - comments_df_no_outliers.min())
    # # slope_comments = coefficients_comments[0]
    # # print('Slope: ' + str(slope_comments))
    # # print('NRMSE Error: ' + str(nrmse_comments))
    # # plt.plot(comments_df_no_outliers)
    # # plt.plot([slope_comments * x + coefficients_comments[1] for x in range(len(comments_df_no_outliers))])
    # # plt.title('LinkedIn Post Comments for ' + link_username)
    # # plt.xlabel('Posts')
    # # plt.ylabel('Comments')
    # # plt.savefig(link_username + '-linkedin-comments-last-' + str(number_of_posts) + '-posts-GRAPH.png', dpi=600)
    # # plt.show()
    # # plt.clf()
    # #
    # # print('**************************')
    # # print('********* VIEWS **********')
    # # print('**************************')
    # # coefficients_views, residuals_views, _, _, _ = np.polyfit(range(len(views_df_no_outliers)), views_df_no_outliers, 1,
    # #                                                           full=True)
    # # mse_views = (residuals_views[0]) / (len(views_df_no_outliers))
    # # nrmse_views = (np.sqrt(mse_views)) / (views_df_no_outliers.max() - views_df_no_outliers.min())
    # # slope_views = coefficients_views[0]
    # # print('Slope: ' + str(slope_views))
    # # print('NRMSE Error: ' + str(nrmse_views))
    # # plt.plot(views_df_no_outliers)
    # # plt.plot([slope_views * x + coefficients_views[1] for x in range(len(views_df_no_outliers))])
    # # plt.title('LinkedIn Post Views for ' + link_username)
    # # plt.xlabel('Posts')
    # # plt.ylabel('Views')
    # # plt.savefig(link_username + '-linkedin-views-last-' + str(number_of_posts) + '-posts-GRAPH.png', dpi=600)
    # # plt.show()
    # # plt.clf()
    #
    # # Save dataframes as CSV files
    # likes_df_no_outliers.to_csv(link_username + '-linkedin-likes-last-' + str(number_of_posts) + '-posts.csv')
    # comments_df_no_outliers.to_csv(link_username + '-linkedin-comments-last-' + str(number_of_posts) + '-posts.csv')
    # views_df_no_outliers.to_csv(link_username + '-linkedin-views-last-' + str(number_of_posts) + '-posts.csv')
    #
    # df_two_only = pd.concat([likes_df_no_outliers, comments_df_no_outliers], axis=1)
    # df_all_three = pd.concat([df_two_only, views_df_no_outliers], axis=1)
    # df_all_three.index.name = 'Post'
    #
    # print(df_all_three)
    #
    # # Actual Graphs
    # app_dash.layout = html.Div([
    #     # Likes Graph:
    #     html.Div([
    #         html.H1("LinkedIn Content Performance", style={'text-align': 'center'}),
    #         html.Br(),
    #         html.H3('Your LinkedIn Likes Performance', style={'text-align': 'center'}),
    #         html.Div(id='output_container', children=['likes_graph', 'views_graph', 'comments_graph']),
    #         dcc.Graph(
    #             figure=dict(
    #                 data=[
    #                     dict(
    #                         x=df_all_three.index,
    #                         y=df_all_three['Likes'],
    #                         name='Likes',
    #                         marker=dict(color='rgb(26, 118, 255)')
    #                     ),
    #                 ],
    #             ),
    #             id='likes_graph'
    #         )
    #     ], className="six columns"),
    #
    #     # Views Graph:
    #     html.Div([
    #         html.H3('Your LinkedIn Views Performance', style={'text-align': 'center'}),
    #         dcc.Graph(
    #             figure=dict(
    #                 data=[
    #                     dict(
    #                         x=df_all_three.index,
    #                         y=df_all_three['Views'],
    #                         name='Views',
    #                         marker=dict(color='rgb(52, 17, 229)')
    #                     ),
    #                 ],
    #             ),
    #             id='views_graph'
    #         )
    #     ], className="six columns"),
    #
    #     # Views Graph:
    #     html.Div([
    #         html.H3('Your LinkedIn Comments Performance', style={'text-align': 'center'}),
    #         dcc.Graph(
    #             figure=dict(
    #                 data=[
    #                     dict(
    #                         x=df_all_three.index,
    #                         y=df_all_three['Comments'],
    #                         name='Comments',
    #                         marker=dict(color='rgb(52, 17, 229)')
    #                     ),
    #                 ],
    #             ),
    #             id='comments_graph'
    #         )
    #     ], className="six columns")
    #
    # ], className="row")
    #
    # return flask.redirect('/dash')


if __name__ == '__main__':
    app.run()
