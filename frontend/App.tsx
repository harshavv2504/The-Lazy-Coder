import React, { useState, useEffect } from 'react';
import { useAudioRecorder } from './hooks/useAudioRecorder';
import RecorderButton from './components/RecorderButton';
import TextCard from './components/TextCard';

// Function to send audio to backend and receive transcription
const sendAudioToBackend = async (audioBlob: Blob): Promise<string> => {
    console.log(`Sending audio of size ${audioBlob.size} bytes to backend.`);
    
    try {
        // Create FormData to send the audio file
        const formData = new FormData();
        formData.append('audio', audioBlob, 'recording.webm');
        
        // Send to backend transcribe endpoint
        const response = await fetch('http://localhost:5000/api/v1/monitoring/transcribe', {
            method: 'POST',
            body: formData,
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Transcription received:', data);
        
        return data.transcription;
        
    } catch (error) {
        console.error('Error sending audio to backend:', error);
        throw new Error(`Failed to transcribe audio: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
};

// Function to send project path to backend
const sendPathToBackend = async (path: string): Promise<void> => {
    console.log(`Sending project context to backend: '${path}'`);
    
    try {
        const response = await fetch('http://localhost:5000/api/v1/monitoring/set-context', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                projectContext: path
            }),
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Project context set successfully:', data);
        
    } catch (error) {
        console.error('Error sending project path to backend:', error);
        throw new Error(`Failed to set project context: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
};


const App: React.FC = () => {
    const [projectPath, setProjectPath] = useState('');
    const [pathSubmitted, setPathSubmitted] = useState(false);
    const [latestTranscription, setLatestTranscription] = useState<string | null>(null);
    const [isProcessing, setIsProcessing] = useState(false);
    const [appError, setAppError] = useState<string | null>(null);
    const [isErrorVisible, setIsErrorVisible] = useState(true);
    
    const { isRecording, audioBlob, startRecording, stopRecording, error: recorderError } = useAudioRecorder();

    const handleError = (errorMessage: string) => {
        setAppError(errorMessage);
    }

    const dismissError = () => {
        setIsErrorVisible(false);
    }

    const handlePathSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        if (!projectPath.trim()) {
            handleError("Please enter a project path or name.");
            return;
        }
        
        setAppError(null);
        setIsProcessing(true);
        
        try {
            await sendPathToBackend(projectPath);
            setPathSubmitted(true);
        } catch (error) {
            handleError(error instanceof Error ? error.message : 'Failed to set project context');
        } finally {
            setIsProcessing(false);
        }
    };

    useEffect(() => {
        if (audioBlob) {
            const processAudio = async () => {
                setIsProcessing(true);
                setAppError(null);
                try {
                    const newText = await sendAudioToBackend(audioBlob);
                    setLatestTranscription(newText);
                } catch (error) {
                    handleError(error instanceof Error ? error.message : 'Failed to transcribe audio');
                } finally {
                    setIsProcessing(false);
                }
            };
            processAudio();
        }
        // This effect should run only when audioBlob changes.
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [audioBlob]);

    // Combine recorder error and app error for display
    const currentError = appError || recorderError;

    // When a new error occurs, make the banner visible again
    useEffect(() => {
        if (currentError) {
            setIsErrorVisible(true);
        }
    }, [currentError]);

    return (
        <div className="h-screen flex flex-col items-center overflow-hidden" style={{backgroundColor: 'var(--bg-primary)', color: 'var(--text-primary)'}}>
            <div 
              className="absolute top-0 left-0 w-full h-full -z-10"
              style={{
                background: `linear-gradient(to bottom right, var(--gradient-from), var(--gradient-to))`,
                clipPath: 'polygon(0 0, 100% 0, 100% 70%, 0% 100%)'
              }}
            ></div>
            
            <div className="w-full flex flex-col items-center flex-shrink-0 z-10 px-4">
                <header className="w-full flex flex-col items-center text-center pt-8 pb-4 animate-fade-in-down">
                    <h1 className="text-4xl md:text-5xl font-bold text-slate-100 tracking-tight">The Lazy Coder</h1>
                </header>

                <form 
                    onSubmit={handlePathSubmit} 
                    className="w-full max-w-md flex items-center gap-2 my-4 animate-fade-in-down" 
                    style={{ animationDelay: '150ms' }}
                >
                    <input
                        type="text"
                        value={projectPath}
                        onChange={(e) => {
                            setProjectPath(e.target.value);
                            if (pathSubmitted) {
                                setPathSubmitted(false); // Allow re-submitting if they change the text
                            }
                        }}
                        placeholder="Enter project path or name..."
                        disabled={pathSubmitted}
                        className="flex-grow rounded-md px-4 py-2 focus:outline-none focus:ring-2 transition-all duration-300 disabled:opacity-70 disabled:cursor-not-allowed"
                        style={{
                            backgroundColor: 'var(--bg-input)',
                            borderColor: 'var(--border-primary)',
                            color: 'var(--text-secondary)',
                            border: '1px solid var(--border-primary)'
                        }}
                        onFocus={(e) => {
                            e.target.style.borderColor = 'var(--accent-primary)';
                            e.target.style.boxShadow = '0 0 0 2px var(--accent-primary)';
                        }}
                        onBlur={(e) => {
                            e.target.style.borderColor = 'var(--border-primary)';
                            e.target.style.boxShadow = 'none';
                        }}
                    />
                    <button
                        type="submit"
                        disabled={pathSubmitted}
                        className="px-4 py-2 rounded-md transition-all duration-300 flex items-center justify-center font-semibold w-24 h-10"
                        style={{
                            backgroundColor: pathSubmitted ? 'var(--accent-primary)' : 'var(--bg-button)',
                            color: pathSubmitted ? 'var(--text-primary)' : 'var(--text-secondary)',
                            cursor: pathSubmitted ? 'default' : 'pointer'
                        }}
                        onMouseEnter={(e) => {
                            if (!pathSubmitted) {
                                e.target.style.backgroundColor = 'var(--bg-button-hover)';
                            }
                        }}
                        onMouseLeave={(e) => {
                            if (!pathSubmitted) {
                                e.target.style.backgroundColor = 'var(--bg-button)';
                            }
                        }}
                        aria-label={pathSubmitted ? "Project context submitted" : "Submit project context"}
                    >
                        {pathSubmitted ? (
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                            </svg>
                        ) : (
                            'Enter'
                        )}
                    </button>
                </form>

                {currentError && isErrorVisible && (
                     <div className="relative flex items-center justify-between rounded-lg px-4 py-2 mb-4 max-w-md w-full animate-fade-in-down"
                          style={{
                              backgroundColor: 'var(--error-bg)',
                              color: 'var(--error-text)',
                              border: '1px solid var(--error-border)'
                          }}>
                        <p className="pr-8">Error: {currentError}</p>
                        <button
                            onClick={dismissError}
                            className="absolute top-1/2 right-2 -translate-y-1/2 p-1 rounded-full text-red-400 hover:bg-red-400/20 transition-colors"
                            aria-label="Dismiss error message"
                        >
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    </div>
                )}
            </div>
            
            <main 
                className="w-full flex-grow flex flex-col items-center justify-center overflow-y-auto relative px-4 pb-4 animate-fade-in-up"
                style={{ animationDelay: '300ms' }}
            >
                {latestTranscription ? (
                    <TextCard key={latestTranscription} text={latestTranscription} />
                ) : (
                    <div className="text-center text-slate-500">
                        <p>Your latest transcription will appear here.</p>
                    </div>
                )}
                <div className="absolute bottom-0 left-0 right-0 h-20 pointer-events-none" 
                     style={{background: `linear-gradient(to top, var(--bg-primary), transparent)`}} />
            </main>

            <div className="w-full flex flex-col items-center justify-center flex-shrink-0 h-36 z-10">
                {isProcessing && (
                     <div className="flex items-center space-x-2 text-slate-400 mb-2">
                        <svg className="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                           <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                           <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                        </svg>
                        <span>Processing audio...</span>
                    </div>
                )}

                <RecorderButton
                    isRecording={isRecording}
                    isProcessing={isProcessing}
                    startRecording={startRecording}
                    stopRecording={stopRecording}
                />
            </div>
        </div>
    );
};

export default App;