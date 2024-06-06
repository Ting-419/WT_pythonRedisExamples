import redis
r = redis.Redis(host='192.168.0.107', port=6379, db=0)
# add scores
r.zadd('leaderboard', {'player1': 100, 'player2': 200, 'player3': 300})
# update score
r.zincrby('leaderboard', 50, 'player1')
# get leaderboard
leaderboard = r.zrevrange('leaderboard', 0, -1, withscores=True)
print(leaderboard)
