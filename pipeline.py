from agents import(
     _build_scraping_agent, 
     _build_search_agent, 
     critic_chain, 
     writer_chain_
)


def run_full_pipeline(topic: str) -> dict:

    stat = {}

    #search agent working 
    print("\n"+" ="*50)
    print("step 1 - search agent is working ...")
    print("="*50)

    search_agent = _build_search_agent()
    search_result = search_agent.invoke({
        "messages" : [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })

    stat["search_results"] = search_result['messages'][-1].content

    print("\n search result ",stat['search_results'])

    #step 2 - reader agent 
    print("\n"+" ="*50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("="*50)

    scrape_agent = _build_scraping_agent()
    scrape_result = scrape_agent.invoke({
            "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{stat['search_results'][:800]}"
        )]
    })

    stat['scraped_content'] = scrape_result['messages'][-1].content

    print("\nscraped content: \n", stat['scraped_content'])


    print("\n"+" ="*50)
    print("step 3 - Writer is drafting the report ...")
    print("="*50)

    research_combined = (
        f"SEARCH RESULT : \n {stat['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {stat['scraped_content']}"
    )

    stat["report"] = writer_chain_.invoke({
        "topic" : topic,
        "research" : research_combined
    })

    print("\n Final Report\n",stat['report'])

    print("\n"+" ="*50)
    print("step 4 - critic is reviewing the report ")
    print("="*50)

    stat["feedback"] = critic_chain.invoke({
        "report":stat['report']
    })

    print("\n critic report \n", stat['feedback'])

    return stat


if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_full_pipeline(topic)