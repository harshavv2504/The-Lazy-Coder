import React from 'react';

interface RecorderButtonProps {
  isRecording: boolean;
  isProcessing: boolean;
  startRecording: () => void;
  stopRecording: () => void;
}

const RecorderButton: React.FC<RecorderButtonProps> = ({ isRecording, isProcessing, startRecording, stopRecording }) => {
  const handleClick = () => {
    if (isRecording) {
      stopRecording();
    } else {
      startRecording();
    }
  };

  const getButtonClasses = () => {
    if (isProcessing) {
      return 'bg-slate-600 cursor-not-allowed';
    }
    if (isRecording) {
      return 'bg-red-600 hover:bg-red-700 animate-pulse';
    }
    return 'bg-slate-700 hover:bg-slate-600';
  };
  
  const IdleIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="1.5">
      <path strokeLinecap="round" strokeLinejoin="round" d="M12 18.75a6 6 0 006-6v-1.5m-6 7.5a6 6 0 01-6-6v-1.5m6 7.5v3.75m-3.75 0h7.5M12 15.75a3 3 0 01-3-3V4.5a3 3 0 016 0v8.25a3 3 0 01-3 3z" />
    </svg>
  );

  const RecordingIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" viewBox="0 0 24 24" fill="currentColor">
      <path fillRule="evenodd" d="M4.5 7.5a3 3 0 013-3h9a3 3 0 013 3v9a3 3 0 01-3 3h-9a3 3 0 01-3-3v-9z" clipRule="evenodd" />
    </svg>
  );

  return (
    <button
      onClick={handleClick}
      disabled={isProcessing}
      className={`w-20 h-20 rounded-full flex items-center justify-center text-white shadow-2xl transform transition-all duration-300 hover:scale-110 focus:outline-none focus:ring-4 focus:ring-opacity-50 ${getButtonClasses()} ${isRecording ? 'focus:ring-red-500' : 'focus:ring-slate-500'}`}
      aria-label={isRecording ? 'Stop recording' : 'Start recording'}
    >
      {isRecording ? <RecordingIcon /> : <IdleIcon />}
    </button>
  );
};

export default RecorderButton;