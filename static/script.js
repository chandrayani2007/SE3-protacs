document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const submitBtnText = document.querySelector('.btn-text');
    const loader = document.querySelector('.loader');
    
    const idleState = document.getElementById('idle-state');
    const activeState = document.getElementById('active-state');
    const errorState = document.getElementById('error-state');
    
    const scoreCircle = document.getElementById('score-circle');
    const scoreText = document.getElementById('score-text');
    const predictionLabel = document.getElementById('prediction-label');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // UI Loading State
        submitBtnText.classList.add('hidden');
        loader.classList.remove('hidden');
        form.querySelector('button').disabled = true;
        
        idleState.classList.add('hidden');
        activeState.classList.add('hidden');
        errorState.classList.add('hidden');
        
        const formData = {
            ligase_smi: document.getElementById('ligase_smi').value.trim(),
            ligase_fa: document.getElementById('ligase_fa').value.trim(),
            target_smi: document.getElementById('target_smi').value.trim(),
            target_fa: document.getElementById('target_fa').value.trim(),
            linker_smi: document.getElementById('linker_smi').value.trim()
        };

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Prediction failed');
            }

            const data = await response.json();
            
            // Show Active State
            activeState.classList.remove('hidden');
            
            // Animate Score
            const score = parseFloat(data.score).toFixed(4);
            const percentage = Math.round(score * 100);
            
            // Reset stroke classes
            scoreCircle.classList.remove('good-degrader', 'bad-degrader');
            predictionLabel.classList.remove('label-good', 'label-bad');
            
            if (data.prediction === 1) {
                scoreCircle.classList.add('good-degrader');
                predictionLabel.textContent = 'Good Degrader';
                predictionLabel.classList.add('label-good');
            } else {
                scoreCircle.classList.add('bad-degrader');
                predictionLabel.textContent = 'Bad Degrader';
                predictionLabel.classList.add('label-bad');
            }
            
            // Trigger animation
            setTimeout(() => {
                scoreCircle.setAttribute('stroke-dasharray', `${percentage}, 100`);
                animateValue(scoreText, 0, score, 1500);
            }, 100);
            
        } catch (error) {
            errorState.classList.remove('hidden');
            errorMessage.textContent = error.message;
        } finally {
            // Restore Button
            submitBtnText.classList.remove('hidden');
            loader.classList.add('hidden');
            form.querySelector('button').disabled = false;
        }
    });

    // Helper function to animate number counting
    function animateValue(obj, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            obj.innerHTML = (progress * (end - start) + start).toFixed(4);
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }
});
