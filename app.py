import babyagi

@babyagi.register_function(
        metadata={"description": "This is a function that returns the string 'world'."}
)
def world():
    return "world"

@babyagi.register_function(
        metadata={"description": "This is a function that returns the string 'hello' and the result of the world function."},
        dependencies=["world"]
)
def hello_world():
    x = world()
    return f"hello {x}"

if __name__ == "__main__":
    app = babyagi.create_app('/dashboard')
    app.run(host='0.0.0.0', port=8080)
