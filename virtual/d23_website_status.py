import requests
from requests import Response 
import asyncio
from asyncio import TimeoutError
from dataclasses import dataclass

@dataclass
class WebsiteResponse:
    url:str 
    status:int | None
    reason: str


async def check_website(url: str) -> WebsiteResponse:
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'

    try:
        response: Response = await asyncio.to_thread(requests.get, url)
        return WebsiteResponse(url, response.status_code, response.reason)
    except Exception as e:
        return WebsiteResponse(url, None, str(e))


async def check_websites(urls:list[str], timeout: float =  5) -> None:
    tasks = [check_website(url) for url in urls]

    try:
        for completed_task in asyncio.as_completed(tasks, timeout = timeout):
            response: WebsiteResponse= await completed_task

            if response.status is not None:
                print(f'{response.url}: ✅ Online ({response.status}, {response.reason})')
            else:
                print(f'Couldn\'t retrieve information for:"{response.url}"')
    
    except TimeoutError:
        print('Timeout reached - some websites took too long.')


async def main() -> None:
    urls: list[str] = [
        'www.indently.io',
        'www.apple.com',
        'www.facebook.com',
        'nonexistent-website-404.com',
        'www.reddit.com',
        'www.github.com',
    ]

    print(f'Checking {len(urls)} websites...')
    await check_websites(urls)
    print('Done!')

if __name__ == '__main__':
    asyncio.run(main())
 

