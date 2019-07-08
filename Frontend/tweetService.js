const URL = 'http://localhost:8000/api/tweets/';

async function getTweets() {
    let params = {
        url: URL,
        dataType: 'json'
    };
    return await $.get(params);
}

async function postTweet(tweet) {
    let params = {
        url: URL,
        data: tweet,
        dataType: 'json'
    };
    return await $.post(params);
}