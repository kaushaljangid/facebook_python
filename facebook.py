#!usr/bin/python
import pyautogui
import facebook
import sys
import requests


def main():
	print("		menu")
	print(" 1. friendlist")
	print(" 2. only post a message")
	print(" 3. id maps friend view post ")
	print(" 4. Get all of the authenticated user's friends")
	print(" 5. Get all the comments from a post")
	print(" 6. Writes 'message' to the active user's wall")	
	print(" 7. like a post")
	print(" 8. comment on post")	
	print(" 9. Upload an image with a caption")
	print(" 10. wall post")

	
	cx_var=raw_input("\033[1;31m [>]\033[1;m Enter your choice: ")
	if(cx_var=="1"):
	 friendlist()
	 main()
	if(cx_var=="2"):
	 messager()
	 main()
	if(cx_var=="3"):
	 listoffriend()
	 main()
	if(cx_var=="4"):
	 friends()
	 main()
	if(cx_var=="5"):
	 seecomment()
	 main()
	if(cx_var=="6"):
	 messagewall()
	 main()
	if(cx_var=="7"):
	 like()
	 main()
	if(cx_var=="8"):
	 commentpost()
	 main()
	if(cx_var=="9"):
	 upload()
	 main()
	if(cx_var=="10"):
	 main1()
	 main()

	if(cx_var !="1" and cx_var !="2" and cx_var !="3" and cx_var !="4" and cx_var !="5" and cx_var !="6" and cx_var !="7" and cx_var !="8" and cx_var !="9" and cx_var !="10"):
	 main()



def main1():
	VALUE = pyautogui.prompt('ENTER THE PAGE ID ')
	cfg ={
		"page_id" : VALUE,
		"access_token" : token
	 }
	api = get_api(cfg)
	msg = pyautogui.prompt('ENTER THE MESSAGE ')
	status = api.put_wall_post(msg)


def get_api(cfg):
	graph = facebook.GraphAPI(cfg['access_token'])
	# the following if you want to post as yourself.
	resp = graph.get_object('me/accounts')
	page_access_token = None
	for page in resp['data']:
		if page['id'] == cfg['page_id']:
			page_access_token = page['access_token']
	graph = facebook.GraphAPI(page_access_token)
	return graph







def friendlist(): #print a friend list
	me = pyautogui.prompt('ENTER YOUR PROFILE ID')
	graph = facebook.GraphAPI(token)
	profile = graph.get_object(me)
	friends = graph.get_connections("me", "friends")
	friend_list = [friend['name'] for friend in friends['data']]
	print friend_list







def messager(): # only post a message
	post_id  = pyautogui.prompt('ENTER YOUR FRIEND ID USERNAME')
	message  = pyautogui.prompt('ENTER YOUR MESSAGE')
	post = graph.get_object(id=post_id)
	print(post[message])



def listoffriend():	#  id maps 
	post_ids = list()
	num  = pyautogui.prompt('ENTER HOW MANY FRIEND POST YOU WAN TO SEE')
	for i in range(int(num)):
	    n = pyautogui.prompt('POST ID')
	    post_ids.append(int(n))
	posts = graph.get_objects(ids=post_ids)	# Each given id maps to an object.
	for post_id in post_ids:
		print(posts[post_id]['created_time'])





def friends():	#Get all of the authenticated user's friends
	friends = graph.get_connections(id='me', connection_name='friends')





def seecomment():	# Get all the comments from a post
	post_id  = pyautogui.prompt('ENTER POST ID')
	comments = graph.get_connections(id=post_id, connection_name='comments')




def messagewall():# Writes 'Hello, world' to the active user's wall.
	fid = pyautogui.prompt('ACTIVE USER WALL IDS')
	MSG = pyautogui.prompt('MESSAGE')
	graph.put_object(parent_object=fid , connection_name='feed', message=MSG)




def like():# like a  post
	comment_id = pyautogui.prompt('ENTER THE ID WHICH U WANT LIKE')
	graph.put_like(object_id = comment_id)



def commentpost():#comment on post
	post_id = pyautogui.prompt('ENTER THE ID OF POST ')
	post_comment = pyautogui.prompt('ENTER YOUR COMMENT')	
	graph.put_comment(object_id = post_id , message = post_comment)



def upload():# Upload an image with a caption.
	msg = pyautogui.prompt('ENTEER YOUR MESSAGE')
	uploadimage = pyautogui.prompt('ENTER THE LOCATION OF IMAGE')
	graph.put_photo(image=open(uploadimage), message = msg)


if __name__ == '__main__':
	token = pyautogui.prompt('ENTER THE ACCECC_TOKEN ')	
	main()
