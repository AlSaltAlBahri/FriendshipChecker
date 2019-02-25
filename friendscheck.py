from twitter import *
import time

print(" Twitter Friendship Checker by Al Salt: ")

# API credentials
consumer_key = "xxx"
consumer_secret = "xxx"
access_key = "xxx"
access_secret = "xxx"

#twitter object
twitter = Twitter(auth = OAuth(access_key,
                  access_secret,
                  consumer_key,
                  consumer_secret))

# users to check
source = "alsalt77"
target = "DevAlSalt"

result = twitter.friendships.show(source_screen_name = source, target_screen_name = target)
#json returned by api
# https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-show
following = result["relationship"]["target"]["following"]
follows   = result["relationship"]["target"]["followed_by"]


print(str(source) + " follows " + str(target) + " : " + str(follows))
print(target + " follows " + str(source) + " : " + str(following))



