from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


import os

load_dotenv()

def main():
    print("Hello from 02-langchain-start!")

    information = """
    "Keanu" redirects here. For other uses, see Keanu (disambiguation).
    Keanu Reeves

    Reeves in 2025
    Born	Keanu Charles Reeves
    September 2, 1964 (age 61)
    Beirut, Lebanon
    Citizenship	Canada
    Occupations	
    Actor musician
    Years active	1984-present
    Works	Full list
    Partners	
    Jennifer Syme (1998-2000, 2001; her death)
    Alexandra Grant (c.2018-present)[a]
    Children	1[b]
    Relatives	Paul Aaron (step-father)
    Awards	Full list
    Musical career
    Genres	Rock
    Instruments	Bass guitar
    Years active	1991-present
    Member of	Dogstar
    Signature

    Keanu Charles Reeves (kee-AH-noo;[7] born September 2, 1964) is a Canadian[c] actor and musician. The recipient of numerous accolades in a career on screen spanning four decades, he is known for his leading roles in action films, his amiable public image, and his philanthropic efforts. In 2020, The New York Times ranked him as the fourth-greatest actor of the 21st century, and in 2022, Time magazine named him one of the 100 most influential people in the world.

    Born in Beirut and raised in Toronto, Reeves made his acting debut in the Canadian television series Hangin' In (1984), before making his feature-film debut in Youngblood (1986). He had his breakthrough role in the science-fiction comedies Bill & Ted's Excellent Adventure (1989) and Bill & Ted's Bogus Journey (1991). He gained praise for playing a hustler in the independent drama My Own Private Idaho (1991) and established himself as an action hero with leading roles in Point Break (1991) and Speed (1994). Following several box-office disappointments, Reeves's performance in the horror film The Devil's Advocate (1997) was well received. Greater stardom came with his role as Neo in The Matrix (1999); Until 2016, Reeves was the highest paid actor for a single production for reprising the role in its 2003 sequels Reloaded and Revolutions. He also played John Constantine in Constantine (2005).

    Reeves made his film directorial debut with Man of Tai Chi (2013). Following a period of limited commercial success, he made a career comeback by playing the titular assassin in the action film series John Wick (2014–present). Reeves voiced Duke Caboom in Toy Story 4 (2019) and portrayed Johnny Silverhand in the video game Cyberpunk 2077 (2020) as well as its expansion. He has since reprised his roles of Ted in Bill & Ted Face the Music (2020) and Neo in The Matrix: Resurrections (2021), and voiced Shadow the Hedgehog in Sonic the Hedgehog 3 (2024).

    In addition to acting, Reeves is a member of the musical band Dogstar, releasing albums including Somewhere Between the Power Lines and Palm Trees (2023). He is the co-writer and creator of the BRZRKR franchise, which started with the original comic book (2021–2023) and since expanded to include numerous spin-offs, including The Book of Elsewhere (2024). An avid motorcyclist, Reeves is the co-founder of the custom manufacturer ARCH Motorcycle. He also co-founded the production company Company Films.
    """
    summary_template = """
        Given the information {information} about a person, I want to create:
        1. A short summary about the person in 2-3 sentences.
        2. 3 interesting facts about the person.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print("------------------------------------")
    print(response)
    print("------------------------------------")
    print(response.content)
    print("------------------------------------")
    


if __name__ == "__main__":
    main()
