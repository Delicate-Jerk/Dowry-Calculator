import gradio as gr

def calculate_worth(income, profession, employment_status, location):
    # Your worth calculation logic here
    profession_weights = {
        "engineer": 0.3,
        "doctor": 0.4,
        "businessman": 0.5,
        "unemployed": 0.1
    }

    employment_weights = {
        "employed": 0.2,
        "unemployed": 0.1
    }

    location_weights = {
        "India": 0.2,
        "USA": 0.4,
        "Australia": 0.3
        # Add more locations and weights as needed
    }

    profession_worth = profession_weights.get(profession, 0)
    employment_worth = employment_weights.get(employment_status, 0)
    location_worth = location_weights.get(location, 0)

    total_worth = (
        0.2 * profession_worth +
        0.2 * employment_worth +
        0.2 * location_worth
    )

    if profession == "doctor":
        total_worth += 400000
    elif profession == "engineer":
        total_worth += 300000
    elif profession == "unemployed":
        total_worth += 100000

    final_worth = total_worth + income * 10
    return f"Your calculated Dowry in rupees: {final_worth:.2f}"

inputs = [
    gr.inputs.Number(label="Monthly Income (in rupees)"),
    gr.inputs.Dropdown(["Engineer", "Doctor", "Businessman", "Unemployed"], label="Profession"),
    gr.inputs.Dropdown(["employed", "unemployed"], label="Employment Status"),
    gr.inputs.Dropdown(["India", "USA", "Australia"], label="Location"),
]

output = gr.outputs.Textbox()

iface = gr.Interface(
    fn=calculate_worth,
    inputs=inputs,
    outputs=output,
    title="Dowry Calculator (by yours truely - A^2)",
    description="Naughty hora k BKL",
)

iface.launch(share=True)
