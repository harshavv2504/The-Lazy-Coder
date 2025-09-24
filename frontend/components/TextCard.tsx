import React, { useState } from 'react';

interface TextCardProps {
  text: string;
}

const TextCard: React.FC<TextCardProps> = ({ text }) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(text).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }).catch(err => {
      console.error('Failed to copy text: ', err);
    });
  };

  const CopyIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
    </svg>
  );

  const CheckIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
    </svg>
  );

  return (
    <div className="relative backdrop-blur-sm rounded-lg p-4 shadow-lg group w-full max-w-2xl animate-fade-in-up"
         style={{
           backgroundColor: 'var(--bg-card)',
           border: '1px solid var(--border-primary)'
         }}>
      <button
        onClick={handleCopy}
        className="absolute top-3 right-3 p-2 rounded-md transition-all duration-200"
        style={{
          backgroundColor: 'var(--bg-button)',
          color: 'var(--text-muted)'
        }}
        onMouseEnter={(e) => {
          e.target.style.backgroundColor = 'var(--bg-button-hover)';
          e.target.style.color = 'var(--text-primary)';
        }}
        onMouseLeave={(e) => {
          e.target.style.backgroundColor = 'var(--bg-button)';
          e.target.style.color = 'var(--text-muted)';
        }}
        aria-label="Copy text"
      >
        {copied ? <CheckIcon /> : <CopyIcon />}
      </button>
      <p className="whitespace-pre-wrap pr-10" style={{color: 'var(--text-secondary)'}}>{text}</p>
    </div>
  );
};

export default TextCard;