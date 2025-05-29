import asyncio
import aiohttp
import ssl
import certifi
import tracemalloc
import cProfile
import pstats
import io

# Create SSL context for secure HTTP
ssl_context = ssl.create_default_context(cafile=certifi.where())

# URLs to fetch
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
]

# Async fetch function
async def fetch(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        async with session.get(url) as response:
            return await response.text()

# Async main function
async def main():
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print("[Sample Output Snippet]:", results[0][:100], "...")

# Profile runner function
def run_profiled():
    print("📊 Starting profiling...")

    # Start memory tracking
    tracemalloc.start()

    # Start CPU profiler
    profiler = cProfile.Profile()
    profiler.enable()

    # Run async main function
    asyncio.run(main())

    # Stop profiling
    profiler.disable()

    # Save CPU profile to file
    profiler.dump_stats("cpu_profile.prof")

    # Show basic CPU stats in console
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats(pstats.SortKey.CUMULATIVE)
    ps.print_stats(10)
    print(s.getvalue())

    # Show top memory allocations
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("🧠 Top memory allocations:")
    for stat in top_stats[:5]:
        print(stat)

    print("✅ Profiling complete. Use `snakeviz cpu_profile.prof` to visualize.")

# Entry point
if __name__ == "__main__":
    run_profiled()
