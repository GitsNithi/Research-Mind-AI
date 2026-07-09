from app.graph.workflow import graph

topic = input("Enter Research Topic: ")

result = graph.invoke(
    {
        "topic": topic
    }
)

print("\n========== Final Report ==========\n")
print(result["report"])