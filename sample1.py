from browser_use import Agent, Browser
from browser_use import BrowserConfig
from langchain_openai import ChatOpenAI
import asyncio

# Basic configuration for the browser
config = BrowserConfig(
    headless=True,  # Run in headless mode
    # disable_security=True  # Uncomment if you want to disable security
)

# Initialize the browser with the specified configuration
browser = Browser(config=config)

async def main():
    # Initialize the agent with the task and language model
    agent = Agent(
        task="What is Langgraph",
        llm=llm,  # Replace with your LLM configuration
        browser=browser,
        generate_gif=False  # Disable GIF generation
    )

    # Run the agent and get results asynchronously
    result = await agent.run()

    # Process results token-wise
    for action in result.action_results():
      print(action.extracted_content,end="\r",flush=True)
      print("\n\n")
        # if action.is_done:
        #     print(action.extracted_content)

    # Close the browser after completion
    await browser.close()

# Run the asynchronous main function
asyncio.run(main()) 





# # OUTPUT DUMP:
# # 
# # 
# # 
# # 
# # 
# # 
# # 🔍  Searched for "What is Langgraph?" in Google





# 📄  Extracted page as markdown
# : ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac879f622b3cb30dd7_cohere-logos-
# idbbhgStc3%201.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdacfdbb3072f5258f66_hugging%20face.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdaceb29ce1602beb431_logo.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac5f6f2a8c34e5575b_wblogo.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdade49955197d2a8941_mosaic.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac5092327565075208_aws.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdacb28fe27c7784c797_goggle%20drive.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac325d487977a3398b_milvus.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac6348e83137a80c17_openai.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac0d888384ad7d31f3_redis.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdacf9d2dfca1d2a4c81_google%20cloud.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac76b6b8b79414144f_datastax%20logo.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac15e6989ae752a9b5_notion%20logo.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac485cb9900ddafda3_anthropic-
# logo.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdade49955197d2a894d_mongodb.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdacaeab9fdc6452063c_supabase.png)

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac879f622b3cb30dd7_cohere-logos-
# idbbhgStc3%201.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdacfdbb3072f5258f66_hugging%20face.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdaceb29ce1602beb431_logo.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac5f6f2a8c34e5575b_wblogo.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdade49955197d2a8941_mosaic.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac5092327565075208_aws.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdacb28fe27c7784c797_goggle%20drive.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac325d487977a3398b_milvus.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac6348e83137a80c17_openai.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac0d888384ad7d31f3_redis.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdacf9d2dfca1d2a4c81_google%20cloud.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac76b6b8b79414144f_datastax%20logo.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac15e6989ae752a9b5_notion%20logo.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdac485cb9900ddafda3_anthropic-
# logo.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdade49955197d2a894d_mongodb.png)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c8fdacaeab9fdc6452063c_supabase.png)

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667b080e4b3ca12dc5d5d439_Langgraph%20UI-2.webp)

# ## Controllable cognitive architecture for any task

# LangGraph's flexible framework supports diverse control flows – single agent,
# multi-agent, hierarchical, sequential – and robustly handles realistic,
# complex scenarios.  
  
# Ensure reliability with easy-to-add moderation and quality loops that prevent
# agents from veering off course.  
  
# Use LangGraph Platform to templatize your cognitive architecture so that
# tools, prompts, and models are easily configurable with LangGraph Platform
# Assistants.

# [See the docs ](https://langchain-ai.github.io/langgraph/)

# ## Designed for human-agent collaboration

# With built-in statefulness, LangGraph agents seamlessly collaborate with
# humans by writing drafts for review and awaiting approval before acting.
# Easily inspect the agent’s actions and "time-travel" to roll back and take a
# different action to correct course.

# [Read a conceptual guide ](https://langchain-
# ai.github.io/langgraph/concepts/agentic_concepts/#human-in-the-loop)

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667c93d559216bb904fe85a8_gif7%20\(1\).gif)

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667c57f274b66a77e2a26b82_CleanShot2024-06-26at17.08.03-ezgif.com-
# video-to-gif-converter.gif)

# ## First class streaming support for better UX design

# Bridge user expectations and agent capabilities with native token-by-token
# streaming and streaming of intermediate steps, helpful for showing agent
# reasoning and actions back to the user as they happen. Use LangGraph
# Platform's API to deliver dynamic and interactive user experiences.

# [Learn more ](https://langchain-ai.github.io/langgraph/how-tos/streaming-
# tokens/)

# ## Why choose LangGraph?

# ### Control, moderate, and guide your agent’s actions.

# Prevent agents from veering off course and ensure reliability with easy-to-add
# moderation and quality loops. Add human-in-the-loop to steer and approve agent
# actions.

# ### Expressive and customizable agent and multi-agent workflows.

# LangGraph’s low level abstractions offer the flexibility needed to create
# sophisticated agents. Design diverse control flows – single, multi-agent,
# hierarchical, sequential – all with one framework.

# ### Persisted context for long-term interactions.

# With its stateful design, LangGraph stores conversation histories and session
# data to maintain context over time and ensure smooth handoffs in agentic
# systems.

# ### First-class streaming support for better UX design.

# Bridge user expectations and agent capabilities with native token-by-token
# streaming of intermediate steps, helpful for showing agent reasoning and
# actions back to the user as they happen.

# ## LangGraph Platform:  
# Deploy & develop agents at scale

# Craft agent-appropriate UXs using LangGraph Platform's APIs. Quickly deploy
# and scale your agent with purpose-built infrastructure. Choose from multiple
# deployment options.

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/67878de387cf10f90c7ad65f_LangGraph---
# Memory-HQ.gif)

# ## Dynamic APIs for designing agent UXs.

# Craft personalized experiences with the long-term memory API to recall
# information across conversation sessions. Expose, update, and rewind your
# app's state for better user visibility, steering, and interaction. Kick off
# long-running background jobs for research-style or multi-step work.

# [See the docs ](https://langchain-ai.github.io/langgraph/how-tos/streaming-
# tokens/)

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/67879a0dd9100d8e643eb39e_LangGraph%20-%20Fault-
# tolerant%20scalability.gif)

# ## Fault-tolerant scalability.

# Handle large workloads gracefully with horizontally-scaling servers, task
# queues, and built-in persistence. Enhance resilience with intelligent caching
# and automated retries.

# [Learn more in the blog ](https://langchain-ai.github.io/langgraph/how-
# tos/streaming-tokens/)

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667c93d559216bb904fe85a8_gif7%20\(1\).gif)

# ## An end-to-end agent experience.

# Simplify prototyping, debugging, and sharing of agents in our visual LangGraph
# Studio. Deploy your application with 1-click deploy with our SaaS offering or
# within your own VPC. Then, monitor app performance with LangSmith.

# [Discover LangGraph Studio ](https://langchain-ai.github.io/langgraph/how-
# tos/streaming-tokens/)

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/66db8c2317fe5b9ad2b84ea0_lcacademylogo.png)

# ## Introduction to LangGraph

# Learn the basics of LangGraph in this LangChain Academy Course. You'll learn
# how to build agents that automate real-world tasks with LangGraph
# orchestration.

# [Enroll for free](https://academy.langchain.com/courses/intro-to-
# langgraph)[Book enterprise
# training](https://airtable.com/appGjCAN6126Jm7K8/pagNAp7niHQzRH8zk/form)

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/6787ae429071ad3575902249_card%201%201.webp)![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/6787ae0bce5c99dd808545ce_card%202.webp)

# ## Deploy agents at scale, monitor carefully, iterate boldly

# Design agent-driven user experiences with LangGraph Platform's APIs. Quickly
# deploy and scale your application with infrastructure built for agents. Choose
# from multiple deployment options.

# ### Fault-tolerant scalability

# Handle large workloads gracefully with horizontally-scaling servers, task
# queues, and built-in persistence. Enhance resilience with intelligent caching
# and automated retries.

# ### Dynamic APIs for designing agent experience

# Craft personalized user experiences with APIs featuring long-term memory to
# recall information across conversation sessions. Track, update, and rewind
# your app's state for easy human steering and interaction. Kick off long-
# running background jobs for research-style or multi-step work.

# ### Integrated developer experience

# Simplify prototyping, debugging, and sharing of agents in our visual LangGraph
# Studio. Deploy your application with 1-click deploy with our SaaS offering or
# within your own VPC. Then, monitor app performance with LangSmith.

# ### Trusted by companies taking agency in AI innovation:

# LangGraph helps teams of all sizes, across all industries, from ambitious
# startups to established enterprises.

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c5308aea1371b447cc4af9_elastic-ar21.png)

# “LangChain is streets ahead with what they've put forward with LangGraph.
# LangGraph sets the foundation for how we can build and scale AI workloads —
# from conversational agents, complex task automation, to custom LLM-backed
# experiences that 'just work'. The next chapter in building complex production-
# ready features with LLMs is agentic, and with LangGraph and LangSmith,
# LangChain delivers an out-of-the-box solution to iterate quickly, debug
# immediately, and scale effortlessly.”

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667b26a1b4576291d6a9335b_garrett%20spong%201.webp)

# Garrett Spong

# Principal SWE

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/6679de9dc4e7bee218d4b058_Norwegian-Cruise-
# Line-Logo%202-2.webp)

# “LangGraph has been instrumental for our AI development. Its robust framework
# for building stateful, multi-actor applications with LLMs has transformed how
# we evaluate and optimize the performance of our AI guest-facing solutions.
# LangGraph enables granular control over the agent's thought process, which has
# empowered us to make data-driven and deliberate decisions to meet the diverse
# needs of our guests.”

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667b265bed5f5a9d26d6b7d6_andres%20torres%201.webp)

# Andres Torres

# Sr. Solutions Architect

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667c6f809f0ebc7b1d72a99b_Replit.png)

# “It's easy to build the prototype of a coding agent, but deceptively hard to
# improve its reliability. Replit wants to give a coding agent to millions of
# users — reliability is our top priority, and will remain so for a long time.
# LangGraph is giving us the control and ergonomics we need to build and ship
# powerful coding agents.”

# “As Ally advances its exploration of Generative AI,

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667c6fcaaa21bcf2fe006dbe_1690576438641%20\(1\)%201.webp)

# Michele Catasta

# President

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/6679e1baf7ea357d0763cde1_ally-
# bank%201-2.png)

# “As Ally advances its exploration of Generative AI, our tech labs is excited
# by LangGraph, the new library from LangChain, which is central to our
# experiments with multi-actor agentic workflows. We are committed to deepening
# our partnership with LangChain.”

# “As Ally advances its exploration of Generative AI,

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/6679e2d31352c6bd56c84280_ally.png)

# Sathish Muthukrishnan

# Chief Information, Data and Digital Officer

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/65c5308aea1371b447cc4af9_elastic-ar21.png)

# “LangChain is streets ahead with what they've put forward with LangGraph.
# LangGraph sets the foundation for how we can build and scale AI workloads —
# from conversational agents, complex task automation, to custom LLM-backed
# experiences that 'just work'. The next chapter in building complex production-
# ready features with LLMs is agentic, and with LangGraph and LangSmith,
# LangChain delivers an out-of-the-box solution to iterate quickly, debug
# immediately, and scale effortlessly.”

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667b26a1b4576291d6a9335b_garrett%20spong%201.webp)

# Garrett Spong

# Principal SWE

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/6679de9dc4e7bee218d4b058_Norwegian-Cruise-
# Line-Logo%202-2.webp)

# “LangGraph has been instrumental for our AI development. Its robust framework
# for building stateful, multi-actor applications with LLMs has transformed how
# we evaluate and optimize the performance of our AI guest-facing solutions.
# LangGraph enables granular control over the agent's thought process, which has
# empowered us to make data-driven and deliberate decisions to meet the diverse
# needs of our guests.”

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667b265bed5f5a9d26d6b7d6_andres%20torres%201.webp)

# Andres Torres

# Sr. Solutions Architect

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667c6f809f0ebc7b1d72a99b_Replit.png)

# “It's easy to build the prototype of a coding agent, but deceptively hard to
# improve its reliability. Replit wants to give a coding agent to millions of
# users — reliability is our top priority, and will remain so for a long time.
# LangGraph is giving us the control and ergonomics we need to build and ship
# powerful coding agents.”

# “As Ally advances its exploration of Generative AI,

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/667c6fcaaa21bcf2fe006dbe_1690576438641%20\(1\)%201.webp)

# Michele Catasta

# President

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/6679e1baf7ea357d0763cde1_ally-
# bank%201-2.png)

# “As Ally advances its exploration of Generative AI, our tech labs is excited
# by LangGraph, the new library from LangChain, which is central to our
# experiments with multi-actor agentic workflows. We are committed to deepening
# our partnership with LangChain.”

# “As Ally advances its exploration of Generative AI,

# ![](https://cdn.prod.website-
# files.com/65b8cd72835ceeacd4449a53/6679e2d31352c6bd56c84280_ally.png)

# Sathish Muthukrishnan

# Chief Information, Data and Digital Officer

# ## LangGraph FAQs

# Do I need to use LangChain to use LangGraph? What’s the difference?

# No. LangGraph is an orchestration framework for complex agentic systems and is
# more low-level and controllable than LangChain agents. LangChain provides a
# standard interface to interact with models and other components, useful for
# straight-forward chains and retrieval flows.

# How is LangGraph different from other agent frameworks?

# Other agentic frameworks can work for simple, generic tasks but fall short for
# complex tasks bespoke to a company’s needs. LangGraph provides a more
# expressive framework to handle companies’ unique tasks without restricting
# users to a single black-box cognitive architecture.

# Does LangGraph impact the performance of my app?

# LangGraph will not add any overhead to your code and is specifically designed
# with streaming workflows in mind.

# Is LangGraph open source? Is it free?

# Yes. LangGraph is an MIT-licensed open-source library and is free to use.

# How are LangGraph and LangGraph Platform different?

# LangGraph is a stateful, orchestration framework that brings added control to
# agent workflows. LangGraph Platform is a service for deploying and scaling
# LangGraph applications, with an opinionated API for building agent UXs, plus
# an integrated developer studio.

# LangGraph (open source)

# LangGraph Platform

# Features

# Stateful orchestration framework for agentic applications

# Scalable infrastructure for deploying LangGraph applications  

# Python and JavaScript

# Python and JavaScript  

# None

# Yes - useful for retrieving & updating state or long-term memory, or creating
# a configurable assistant  

# Basic

# Dedicated mode for token-by-token messages  

# Community contributed

# Supported out-of-the-box  

# Self-managed

# Managed Postgres with efficient storage  

# Self-managed

# \- Cloud SaaS  
# \- Free self-hosted  
# \- Enterprise  
# (BYOC or paid self-hosted)  

# Self-managed

# Auto-scaling of task queues and servers  

# Self-managed

# Automated retries  

# Simple threading

# Supports double-texting  

# None

# Cron scheduling  

# None

# Integrated with LangSmith for observability  

# LangGraph Studio for Desktop

# LangGraph Studio for Desktop & Cloud  

# What are my deployment options for LangGraph Platform?

# We currently have the following deployment options for LangGraph applications:  
  
# ‍**Self-Hosted Lite** : A free (up to 1M nodes executed), limited version of
# LangGraph Platform that you can run locally or in a self-hosted manner. This
# version requires a LangSmith API key and logs all usage to LangSmith. Fewer
# features are available than in paid plans.  
# ‍**Cloud SaaS:** Fully managed and hosted as part of LangSmith, with automatic
# updates and zero maintenance.  
# ‍**Bring Your Own Cloud (BYOC):** Deploy LangGraph Platform within your VPC,
# provisioned and run as a service. Keep data in your environment while
# outsourcing the management of the service.  
# **Self-Hosted Enterprise:** Deploy LangGraph entirely on your own
# infrastructure.

# Is LangGraph Platform open source?

# No. LangGraph Platform is proprietary software.  
  
# There is a free, self-hosted version of LangGraph Platform with access to
# basic features. The Cloud SaaS deployment option is free while in beta, but
# will eventually be a paid service. We will always give ample notice before
# charging for a service and reward our early adopters with preferential
# pricing. The Bring Your Own Cloud (BYOC) and Self-Hosted Enterprise options
# are also paid services. [Contact our sales team](/contact-sales) to learn
# more.  
  
# For more information, see our [LangGraph Platform pricing page](/pricing-
# langgraph-platform).

# ## Ready to start shipping reliable GenAI apps faster?

# Get started with LangChain, LangSmith, and LangGraph to enhance your LLM app
# development, from prototype to production.

# [Contact Us](/contact-sales)[Sign Up](https://smith.langchain.com/)





# LangGraph is a flexible framework designed for building and scaling agentic applications. It allows for complex task handling and human-agent collaboration, supporting various control flows such as single-agent, multi-agent, hierarchical, and sequential. Key features include:

# - **Statefulness**: LangGraph agents maintain context over time, enabling smooth interactions.
# - **Streaming Support**: It provides native token-by-token streaming for better user experience.
# - **Moderation and Quality Loops**: These features ensure agents remain reliable and on course.
# - **Dynamic APIs**: LangGraph offers APIs for crafting personalized user experiences and managing long-term memory.
# - **Deployment Options**: It supports various deployment methods, including self-hosted and cloud solutions.
 


