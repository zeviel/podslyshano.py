import requests

class Podslyshano:
	def __init__(self) -> None:
		self.api = "https://podslyshano.com/api/v3.3"
		self.headers = {
			"user-agent": "okhttp/4.9.1",
			"x-client-version": "and3.3.2.2",
			"connection": "Keep-Alive"
		}
		self.user_id = None
		self.auth_token = None

	def login(self, email: str, password: str) -> dict:
		response = requests.post(
			f"{self.api}/auth/sign_in?type=email&email={email}&password={password}",
			headers=self.headers).json()
		if "user" in response:
			self.user_id = response["user"]["id"]
			self.auth_token = response["user"]["auth_token"]
			self.headers["authorization"] = self.auth_token
		return response

	def register(
			self,
			email: str,
			password: str,
			device_type: str = "android",
			captcha: str = None,
			captcha_key: str = None) -> dict:
		url = f"{self.api}/auth/sign_up?device_type={device_type}&type=email&email={email}&password={password}"
		if captcha:
			url += f"&captcha={captcha}"
		if captcha_key:
			url += f"&captcha_key={captcha_key}"
		return requests.post(url, headers=self.headers).json()

	def get_account_profile(self) -> dict:
		return requests.get(
			f"{self.api}/profile/me",
			headers=self.headers).json()

	def get_new_posts(self) -> dict:
		return requests.get(
			f"{self.api}/posts",
			headers=self.headers).json()

	def get_random_posts(self) -> dict:
		return requests.get(
			f"{self.api}/posts/random",
			headers=self.headers).json()

	def get_best_posts(self) -> dict:
		return requests.get(
			f"{self.api}/posts/top/day",
			headers=self.headers).json()

	def get_categories(self) -> dict:
		return requests.get(
			f"{self.api}/profile/categories",
			headers=self.headers).json()

	def get_post_likes(self, post_id: int) -> dict:
		return requests.get(
			f"{self.api}/posts/{post_id}/likes",
			headers=self.headers).json()

	def add_to_bookmarks(
			self,
			post_id: int = None,
			comment_id: int = None) -> dict:
		if post_id:
			url = f"{self.api}/bookmarks/posts?id={post_id}"
		elif comment_id:
			url = f"{self.api}/bookmarks/comments?id={comment_id}"
		return requests.post(url, headers=self.headers).json()

	def delete_from_bookmarks(
			self,
			post_id: int = None,
			comment_id: int = None) -> dict:
		if post_id:
			url = f"{self.api}/bookmarks/posts/{post_id}"
		elif comment_id:
			url = f"{self.api}/bookmarks/comments/{comment_id}"
		return requests.delete(url, headers=self.headers).json()

	def like_post(
			self,
			post_id: int,
			type: str) -> dict:
		return requests.post(
			f"{self.api}/posts/{post_id}/like?type={type}",
			headers=self.headers).json()

	def unlike_post(self, post_id: int) -> dict:
		return requests.delete(
			f"{self.api}/posts/{post_id}/like",
			headers=self.headers).json()

	def get_post_comments(self, post_id: int) -> dict:
		return requests.get(
			f"{self.api}/posts/{post_id}/comments",
			headers=self.headers).json()

	def get_post_latest_comments(self, post_id: int) -> dict:
		return requests.get(
			f"{self.api}/posts/{post_id}/comments/latest",
			headers=self.headers).json()

	def get_post_best_comments(self, post_id: int) -> dict:
		return requests.get(
			f"{self.api}/posts/{post_id}/comments/top",
			headers=self.headers).json()

	def get_email_confirmation(self) -> dict:
		return requests.post(
			f"{self.api}/profile/email_confirmation",
			headers=self.headers).json()

	def comment_post(
			self,
			post_id: int,
			text: str,
			parent_id: int = None) -> dict:
		data = {
			"text_fixed": text
		}
		if parent_id:
			data["parent_id"] = parent_id
		return requests.post(
			f"{self.api}/posts/{post_id}/comments",
			data=data,
			headers=self.headers).json()

	def change_email(self, email: str) -> dict:
		return requests.put(
			f"{self.api}/profile/me?user[email]={email}",
			headers=self.headers).json()

	def report_comment(self, comment_id: int) -> dict:
		return requests.post(
			f"{self.api}/comments/{comment_id}/complain",
			headers=self.headers).json()

	def like_comment(self, comment_id: int) -> dict:
		return requests.post(
			f"{self.api}/comments/{comment_id}/like",
			headers=self.headers).json()

	def unlike_comment(self) -> dict:
		return requests.delete(
			f"{self.api}/comments/{comment_id}/cancel_like",
			headers=self.headers).json()

	def get_user_profile(self, user_id: int) -> dict:
		return requests.get(
			f"{self.api}/profile/{user_id}",
			headers=self.headers).json()

	def block_user(self, user_id: int) -> int:
		return requests.post(
			f"{self.api}/profile/{user_id}/ban",
			headers=self.headers).status_code

	def unblock_user(self, user_id: int) -> int:
		return requests.post(
			f"{self.api}/profile/{user_id}/unban",
			headers=self.headers).status_code

	def get_user_comments(self, user_id: int) -> dict:
		return requests.get(
			f"{self.api}/comments/for_user/{user_id}",
			headers=self.headers).json()

	def get_user_likes(self, user_id: int) -> dict:
		return requests.get(
			f"{self.api}/posts/liked?user_id={user_id}",
			headers=self.headers).json()

	def report_user(self, user_id: int, reason: str) -> dict:
		return requests.post(
			f"{self.api}/profile/{user_id}/complain?reason_text={reason}",
			headers=self.headers).json()

	def post_secret(self, note: str) -> dict:
		data = {"note": note}
		return requests.post(
			f"{self.api}/secrets",
			data=data,
			headers=self.headers).json()

	def get_notifications(self) -> dict:
		return requests.get(
			f"{self.api}/activities",
			headers=self.headers).json()

	def get_block_list(self) -> dict:
		return requests.get(
			f"{self.api}/profile/banned_users",
			headers=self.headers).json()

	def edit_profile(
			self,
			bio: str = None,
			nickname: str = None,
			show_comments: bool = False,
			show_likes: bool = True) -> dict:
		url = f"{self.api}/profile/me?user[show_comments]={show_comments}&user[show_likes]={show_likes}"
		if bio:
			url += f"&user[bio]={bio}"
		if nickname:
			url += f"&user[fullname]={nickname}"
		return requests.put(url, headers=self.headers).json()
