from jaseci_ai_kit import t5_sum

def summarize_text(text, min_length=40, max_length=120):
    """
    Summarizes the given text using the Jaseci T5 summarizer.
    """
    try:
        summary = t5_sum.t5_generate_sum(text, min_length, max_length)
        return summary
    except Exception as e:
        return f"Error generating summary: {e}"

if __name__ == "__main__":
    sample_text = (
        "Artificial intelligence enables machines to perform tasks that "
        "typically require human intelligence, such as visual perception, "
        "speech recognition, and decision-making. It has numerous applications "
        "across healthcare, finance, education, and agriculture."
    )

    print("\n--- Summary ---")
    print(summarize_text(sample_text))
