import React, { useState } from "react";
import axios from "axios";

const questions = [
  "How often do you travel?",
  "How much trash do you produce?",
  "How much energy do you consume?",
  "How much water do you use?",
  "Do you have plants at home?",
];

const Questionnaire: React.FC<{
  setScores: (scores: { [key: string]: number }) => void;
}> = ({ setScores }) => {
  const options = (obj: Object) => ({
    method: "GET",
    header: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(obj),
  });

  const mockApiCall = async (answers: string[]) => {
    const apiResponse = await Promise.all([
      axios(
        "http://127.0.0.1:5000/travel",
        options({
          "answers1": answers[0]
      })
      ),
      axios(
        "http://127.0.0.1:5000/trash",
        options({
          "answers2":answers[1]
      })
      ),
      axios(
        "http://127.0.0.1:5000/energy",
        options({
          "answers3":answers[2]
        })
      ),
      axios(
        "http://127.0.0.1:5000/water",
        options({
          "answers4":answers[3]
        })
      ),
      axios(
        "http://127.0.0.1:5000/plants",
        options({
          "answers5":answers[4]
        })
      ),
    ]);

    console.log(apiResponse);

    // const travelScore = apiResponse.data.travel || Math.floor(Math.random() * 100);

    return {
      travel: Math.floor(Math.random() * 100),
      trash: Math.floor(Math.random() * 100),
      energy: Math.floor(Math.random() * 100),
      water: Math.floor(Math.random() * 100),
      plant: Math.floor(Math.random() * 100),
    };
  };
  const [answers, setAnswers] = useState<string[]>(
    Array(questions.length).fill("")
  );
  const [currentQuestion, setCurrentQuestion] = useState<number>(0);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newAnswers = [...answers];
    newAnswers[currentQuestion] = e.target.value;
    setAnswers(newAnswers);
  };

  const handleSubmit = async () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      const scores = await mockApiCall(answers);
      setScores(scores);
    }
  };

  return (
    <div>
      <h1>Carbon Footprint Questionnaire</h1>
      <p>{questions[currentQuestion]}</p>
      <input
        type="text"
        value={answers[currentQuestion]}
        onChange={handleChange}
      />
      <button onClick={handleSubmit}>Next</button>
    </div>
  );
};

export default Questionnaire;
