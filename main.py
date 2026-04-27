from research_server import mcp


def main():
    print("Starting research server on http://0.0.0.0:8001/mcp")
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()