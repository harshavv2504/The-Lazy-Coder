# The Lazy Coder - Backend Integration Guide (Final)

## 1. Introduction

This document provides the final technical specification for integrating a backend service with **The Lazy Coder** React frontend. It outlines the necessary API endpoints, data formats, and error handling protocols. The frontend is currently implemented with mock functions that must be replaced with live API calls as described below.

## 2. Prerequisites

-   **Audio Format**: The frontend captures audio and sends it as a `Blob` with the MIME type `audio/webm`. The backend transcription service must be able to process this format.

## 3. API Endpoints Summary

| Feature                 | Frontend Integration Point              | Endpoint (Example) | Method | Request Body                             | Success Response                | Notes                                        |
| ----------------------- | --------------------------------------- | ------------------ | ------ | ---------------------------------------- | ------------------------------- | -------------------------------------------- |
| **Project Context**     | `App.tsx`<br>`sendPathToServer`       | `/set-context`     | `POST` | JSON: `{ "projectContext": "..." }`  | `204 No Content` or `200 OK`    | Sets the user's project context for the session. |
| **Audio Transcription** | `App.tsx`<br>`sendAudioToBackend`      | `/transcribe`      | `POST` | `FormData` with `audio` field (`.webm`)  | `200 OK` with JSON: `{ "transcription": "..." }` | The main transcription service.              |

---

## 4. Integration Details

All integration logic is centralized in **`App.tsx`**. The goal is to replace the mock functions with your production API calls.

### 4.1. Set Project Context

This endpoint is called when the user submits their project path or name. It informs the backend of the current working context.

-   **Function to Replace**: `mockSendPathToServer` inside `App.tsx`.
-   **Called From**: `handlePathSubmit` function.

**Example `sendPathToServer` Implementation:**
```typescript
const sendPathToServer = async (projectContext: string): Promise<void> => {
    const response = await fetch('YOUR_API_ENDPOINT/set-context', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // 'Authorization': 'Bearer YOUR_API_TOKEN', // Add auth if needed
        },
        body: JSON.stringify({ projectContext }),
    });

    if (!response.ok) {
        // The frontend will catch this and display an error.
        // For specific messages, see the Error Handling Protocol section.
        const errorData = await response.json().catch(() => ({})); // Gracefully handle non-JSON error bodies
        const errorMessage = errorData.error || `Failed to set project context. Status: ${response.status}`;
        throw new Error(errorMessage);
    }
};
```

### 4.2. Transcribe Audio

This is the primary endpoint. It accepts a recorded audio file and returns the transcribed text.

-   **Function to Replace**: `mockSendAudioToBackend` inside `App.tsx`.
-   **Called From**: `useEffect` hook that observes `audioBlob`.

**Example `sendAudioToBackend` Implementation:**
```typescript
const sendAudioToBackend = async (audioBlob: Blob): Promise<string> => {
    const formData = new FormData();
    // The field name 'audio' must match the backend's expected field.
    formData.append('audio', audioBlob, 'recording.webm');

    const response = await fetch('YOUR_API_ENDPOINT/transcribe', {
        method: 'POST',
        body: formData,
        // headers: { 'Authorization': 'Bearer YOUR_API_TOKEN' }, // Add auth if needed
    });

    if (!response.ok) {
        const errorData = await response.json().catch(() => ({})); // Gracefully handle non-JSON error bodies
        const errorMessage = errorData.error || `Audio processing failed. Status: ${response.status}`;
        throw new Error(errorMessage);
    }

    const data = await response.json();
    if (!data.transcription) {
        throw new Error("Invalid response from server: 'transcription' field missing.");
    }
    return data.transcription;
};
```
*You must replace the placeholder `YOUR_API_ENDPOINT` with your actual service URL.*

---

## 5. Critical: Error Handling Protocol

To provide a high-quality user experience, the backend **must** communicate errors using standard HTTP status codes and a consistent JSON error format. The frontend is designed to parse these responses and display user-friendly messages.

### 5.1. General Mechanism

1.  The backend returns a `4xx` or `5xx` HTTP status code.
2.  The backend response body should be a JSON object with an `error` key:
    ```json
    {
      "error": "A clear, user-facing error message."
    }
    ```
3.  The frontend's `fetch` call will see `!response.ok` is `true`.
4.  The frontend will attempt to parse the JSON body to extract the value of the `error` key.
5.  This message is displayed to the user in the error banner. If the JSON is invalid or the `error` key is missing, a generic fallback message is shown.

### 5.2. Example Error Scenarios

| Status Code | Meaning                      | Example Backend Response Body (`JSON`)                       | Frontend Message Displayed                                    |
| ----------- | ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------- |
| `400`       | **Bad Request**              | `{"error": "Invalid audio format. Please use WEBM."}`        | `Error: Invalid audio format. Please use WEBM.`               |
| `401`       | **Unauthorized**             | `{"error": "Authentication failed. Please check your API key."}` | `Error: Authentication failed. Please check your API key.`    |
| `429`       | **Too Many Requests**        | `{"error": "Rate limit exceeded. Please try again later."}`  | `Error: Rate limit exceeded. Please try again later.`         |
| `500`       | **Internal Server Error**    | `{"error": "Transcription service is currently unavailable."}` | `Error: Transcription service is currently unavailable.`      |
| `503`       | **Service Unavailable**      | `{"error": "The server is temporarily down for maintenance."}` | `Error: The server is temporarily down for maintenance.`      |

By adhering to this protocol, you ensure that the user receives meaningful feedback when an operation fails, leading to a more robust and professional application.
