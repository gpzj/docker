FROM instapy/instapy
ARG FILEPATH
COPY $FILEPATH/insta_like_whitneys_posts.py /
COPY $FILEPATH/requirements.txt /
RUN pip install -r /requirements.txt
CMD [ "python", "/insta_like_whitneys_posts.py" ]
