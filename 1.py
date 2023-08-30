import gradio as gr

def calculate_worth(income, profession_weight, employment_weight, location_weight, profession, employment_status, location):
    profession_weights = {
        "engineer": profession_weight,
        "doctor": profession_weight,
        "businessman": profession_weight,
        "unemployed": profession_weight
    }

    employment_weights = {
        "employed": employment_weight,
        "unemployed": employment_weight
    }

    location_weights = {
        "India": location_weight,
        "USA": location_weight,
        "Australia": location_weight
        # Add more locations and weights as needed
    }

    profession_worth = profession_weights.get(profession, 0)
    employment_worth = employment_weights.get(employment_status, 0)
    location_worth = location_weights.get(location, 0)

    total_worth = (
        profession_worth +
        employment_worth +
        location_worth
    )

    if profession == "doctor":
        total_worth += 400000
    elif profession == "engineer":
        total_worth += 300000
    elif profession == "unemployed":
        total_worth += 100000

    final_worth = total_worth + income * 10
    return f"Your calculated worth in rupees: {final_worth:.2f}"

inputs = [
    gr.inputs.Number(label="Monthly Income (in rupees)"),
    gr.inputs.Slider(minimum=0, maximum=1, default=0.5, label="Profession Weight"),
    gr.inputs.Slider(minimum=0, maximum=1, default=0.5, label="Employment Weight"),
    gr.inputs.Slider(minimum=0, maximum=1, default=0.5, label="Location Weight"),
]

output = gr.outputs.Textbox()

iface = gr.Interface(
    fn=calculate_worth,
    inputs=inputs,
    outputs=output,
    title="Worth Calculator with Custom Weights",
    description="Calculate your worth based on income, profession, employment status, and location with custom weights.",
)

iface.launch()
