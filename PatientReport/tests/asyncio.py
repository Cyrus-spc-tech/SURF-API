import asyncio

#coroutine fx 

async def fetch_data(delay):
    print("Fetching . . . ")
    await asyncio.sleep(delay)
    print("Fetched Data")
    return {"data":"example"}



async def main():
    print("start of main corout:")
    task = fetch_data(2)
    result=await task

    print(f"res:{result}")
    print("end")


asyncio.run(main())








# coroutine
asyncio.run(main())