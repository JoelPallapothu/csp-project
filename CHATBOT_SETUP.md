# CAVI Cyber Safety Assistant — AI & API Setup Guide

This guide explains how to securely configure the AI integration for the **CAVI Cyber Safety Assistant** on both your local development machine and **Streamlit Community Cloud**.

---

## 1. AI Provider Used
The CAVI Cyber Safety Assistant supports modern, lightweight, and cost-effective LLM APIs:
- **Google Gemini API** (Recommended: `gemini-1.5-flash` or `gemini-2.0-flash`)
- **OpenAI API** (Alternative: `gpt-4o-mini`)

The assistant operates with strict safety guardrails, emergency detection (auto-routing financial loss queries to **📞 1930** and **cybercrime.gov.in**), sensitive data filtering, and zero-crash fallback to our curated bilingual knowledge base.

---

## 2. Required Secret Structure
The application automatically reads the API key from Streamlit Secrets in any of the following standard formats:

### Recommended Format:
```toml
[api]
key = "YOUR_API_KEY"
```

### Alternative Accepted Formats:
```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```
or
```toml
OPENAI_API_KEY = "YOUR_API_KEY"
```

> [!IMPORTANT]
> `"YOUR_API_KEY"` is a placeholder. Replace it with your actual secret key obtained from Google AI Studio (`https://aistudio.google.com/`) or OpenAI Platform. **Never publish or commit real API keys.**

---

## 3. Local Development Setup
To test the live AI model on your local machine:

1. In the project root directory, create a hidden folder named `.streamlit` (if it does not already exist):
   ```bash
   mkdir .streamlit
   ```
2. Inside `.streamlit`, create a file named `secrets.toml`:
   ```toml
   [api]
   key = "YOUR_API_KEY"
   ```
3. Run Streamlit:
   ```bash
   streamlit run app.py
   ```

---

## 4. Streamlit Community Cloud Setup
When deploying CAVI to **Streamlit Community Cloud** (`share.streamlit.io`):

1. Go to your app dashboard at [share.streamlit.io](https://share.streamlit.io).
2. Click on the three dots next to your app `⋮` and select **Settings**.
3. In the left navigation menu of the modal, click **Secrets**.
4. Paste the configuration into the Secrets text box:
   ```toml
   [api]
   key = "YOUR_ACTUAL_API_KEY_HERE"
   ```
5. Click **Save**. The app will automatically reload and securely use the key without exposing it in source code.

---

## 5. GitHub Security & Zero-Leak Protection
- `.streamlit/secrets.toml` is included in the project's [`.gitignore`](file:///.gitignore).
- Git will **never** track or commit `secrets.toml`.
- If no API key is provided, the application **does not crash**; it displays the friendly notice:
  - **English**: *"AI chatbot configuration is not available yet. You can still use the CAVI Safety Guide and emergency reporting information."*
  - **Telugu**: *"AI చాట్బాట్ కాన్ఫిగరేషన్ ఇంకా అందుబాటులో లేదు. మీరు CAVI Safety Guide మరియు అత్యవసర రిపోర్టింగ్ సమాచారాన్ని ఉపయోగించవచ్చు."*
  and immediately answers using its built-in curated cyber-safety knowledge base.
