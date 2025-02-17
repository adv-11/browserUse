import os
import sys
from pathlib import Path
from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext
from browser_use.agent.views import ActionResult
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio
from langchain_openai import ChatOpenAI



browser = Browser(
	config=BrowserConfig(
		# NOTE: insert your path here, leaving mine blank for commit :D
		chrome_instance_path=':D',
	)
)


async def main():
	agent = Agent(
		task='In docs.google.com write a quick letter',
		llm=ChatOpenAI(model='gpt-4o'),
		browser=browser,
	)

	await agent.run()
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())