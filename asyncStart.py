import aiohttp,asyncio
class asyncStart():
	def __init__(self):
		self.session = aiohttp.ClientSession()
		self.api="https://api.start.ru"
		self.api_key="a20b12b279f744f2b3c7b5c5400c4eb5"
		self.profile_id=None
		self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "application/json"}
	def __del__(self):
		try:
		          loop = asyncio.get_event_loop()
		          loop.create_task(self._close_session())
		except RuntimeError:
		          loop = asyncio.new_event_loop()
		          loop.run_until_complete(self._close_session())
	async def _close_session(self):
		if not self.session.closed: await self.session.close()
	async def get_languages(self):
		async with self.session.get(f"{self.api}/languages/content?apikey={self.api_key}",headers=self.headers) as req:
			return await req.json()
	async def no_trailer(self):
		async with self.session.get(f"{self.api}/notrailer?apikey={self.api_key}",headers=self.headers) as req:
			return await req.json()
	async def profile_list(self):
		async with self.session.get(f"{self.api}/notrailer?apikey={self.api_key}",headers=self.headers) as req:
			return await req.json()
	async def account_subscriptions(self):
		async with self.session.get(f"{self.api}/v2/account/subscriptions?apikey={self.api_key}",headers=self.headers) as req:
			return await req.json()
	async def billing_subscriptions(self):
		async with self.session.get(f"{self.api}/billing/subscriptions?apikey={self.api_key}",headers=self.headers) as req:
			return await req.json()
	async def refresh_account(self):
		async with self.session.get(f"{self.api}/auth/refresh?apikey={self.api_key}",headers=self.headers) as req:
			return await req.json()
	async def login(self,email,password):
		data={"password":password,"device_id":"864bb95c-d211-4abf-9385-2e58aad955cb","device_type":"web","client_platform":"start","email":email,"is_encoded":False}
		async with self.session.post(f"{self.api}/v2/auth/email/login?apikey={self.api_key}",json=data,headers=self.headers) as req:
			self.headers['Cookie']= await req.headers['Set-Cookie']
			self.profile_id= await req.json()['profile_id']
			return await req.json()
	async def register(self,email,password):
		data={"email":email,"password":password,"device_id":"eb95581b-85bc-4d4f-983e-b58edbaf4125","device_type":"web","client_platform":"start","is_encoded":False}
		async with self.session.post(f"{self.api}/v2/auth/email/register?apikey={self.api_key}",json=data,headers=self.headers) as req:
			self.headers['Cookie']= await req.headers['Set-Cookie']
			self.profile_id= await req.json()['profile_id']
			return await req.json()
	async def edit_profile(self,birthday:str=None,gender:str=None,name:str=None):
		if birthday:
			data={"birthday":birthday}
			async with self.session.put(f"{self.api}/account/person/birthday?apikey={self.api_key}",json=data,headers=self.headers) as req:
				return await req.json()
		if gender:
			data={"gender":gender}
			async with self.session.put(f"{self.api}/account/person/gender?apikey={self.api_key}",json=data,headers=self.headers) as req:
				return await req.json()
		if name:
			data={"name":name}
			async with self.session.put(f"{self.api}/account/person/name?apikey={self.api_key}",json=data,headers=self.headers) as req:
				return await req.json()
	async def reset_password(self,email):
		data={"device_id":"359847a8-7395-40bf-820b-bbbc21294f24","device_type":"web","client_platform":"start","email":email}
		async with self.session.post(f"{self.api}/auth/password/reset?apikey={self.api_key}",json=data,headers=self.headers) as req:
			return await req.json()
	async def favirites(self,product_id):
		data={"product_id":product_id}
		async with self.session.post(f"{self.api}/profile/favorites/{self.profile_id}?apikey={self.api_key}",json=data,headers=self.headers) as req:
			return await req.json()
	async def rate_content(self,content_id,like:str=True):
		data={"profile_id":self.profile_id,"content_id":content_id,"like":like}
		async with self.session.post(f"{self.api}/v2/profile/rate-content?apikey={self.api_key}",json=data,headers=self.headers) as req:
			return await req.json()
	async def heroes(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		async with self.session.get(f"{self.api}/heroes?apikey={self.api_key}&for_kids={for_kids}&locale={locale}&content_lang={content_lang}",headers=self.headers)as req:
			return await req.json()
	async def posmotret_segodnya(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		async with self.session.get(f"{self.api}/v2/showcase/chto-posmotret-segodnya?apikey={self.api_key}&locale={locale}&content_lang={content_lang}&profile_id={self.profile_id}&device_type=web&for_kids={for_kids}",headers=self.headers) as req:
			return await req.json()
	async def banner_featured(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		async with self.session.get(f"{self.api}/banner/featured?apikey={self.api_key}&for_kids={for_kids}&locale={locale}&content_lang={content_lang}&device_type=web",headers=self.headers) as req:
			return await req.json()
	async def chyotkie_films(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		async with self.session.get(f"{self.api}/v2/showcase/chyotkie-filmy-i-serialy?apikey={self.api_key}&locale={locale}&content_lang={content_lang}&profile_id={self.profile_id}&device_type=web&for_kids={for_kids}",headers=self.headers) as req:
			return await req.json()
	async def start_predstavlyaet(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		async with self.session.get(f"{self.api}/v2/showcase/start-predstavlyaet-web?apikey={self.api_key}&locale={locale}&content_lang={content_lang}&profile_id={self.profile_id}&device_type=web&for_kids={for_kids}",headers=self.headers) as req:
			return await req.json()
	async def trending(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		async with self.session.get(f"{self.api}/trending?apikey={self.api_key}&for_kids={for_kids}&locale={locale}&content_lang={content_lang}",headers=self.headers) as req:
			return await req.json()
	async def recommendation(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		async with self.session.get(f"{self.api}/recommendation/exp1/featured/{self.profile_id}?apikey={self.api_key}&for_kids={for_kids}&locale={locale}&content_lang={content_lang}",headers=self.headers) as req:
			return await req.json()