from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain


def run_research_pipeline(topic : str) -> dict:

    state = {}

    # search agent working

    print("\n" + "="*50)
    print("step 1  Search Agent is working ......")


    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages" : [("user", f"Find recent, reliable and detailed information about : {topic}")]
    })

    state["search_result"] = search_result["messages"][-1].content

    # reader agent 
    print("\n" + "="*50)
    print("step 2  Reader Agent is working ......")    

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [
            (
                "user",
                (
                    f"Based on the following search results about {topic}. "
                    f"Pick the most relevant URL and scrape it for deeper content.\n\n"
                    f"Search Result:\n{state['search_result'][:800]}"
                )
            )
        ]
    })

    state["scraped_content"] = reader_result["messages"][-1].content

    # step 3 : writer chain 
    print("==========================================")
    print("Step 3 Writer content started ......")

    research_combined = (
        f"SEARCH RESULT : \n {state["search_result"]} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic" : topic,
        "research" : research_combined
    })

    print("\n Final Report \n", state["report"])


    # critic report

    print("============================================================")
    print("Step 4 Critical evalution of report is started ......")


    state["feedback"] = critic_chain.invoke({
        "report" : state["report"]
    })

    print("===============================================")
    print("Feedback Report ......")
    print(state["feedback"])

    return state


if __name__=="__main__":
    topic = input("Enter research topic: ")
    run_research_pipeline(topic)


