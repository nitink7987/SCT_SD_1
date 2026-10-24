"use strict";

const form = document.querySelector("#converter-form");
const temperatureInput = document.querySelector("#temperature");
const fromUnitSelect = document.querySelector("#from-unit");
const toUnitSelect = document.querySelector("#to-unit");
const resultOutput = document.querySelector("#result");
const errorMessage = document.querySelector("#error-message");
const resetButton = document.querySelector("#reset-button");

const symbols = {
  Celsius: "°C",
  Fahrenheit: "°F",
  Kelvin: "K"
};

function convertTemperature(value, fromUnit, toUnit) {
  let celsius;

  if (fromUnit === "Celsius") {
    celsius = value;
  } else if (fromUnit === "Fahrenheit") {
    celsius = (value - 32) * 5 / 9;
  } else {
    celsius = value - 273.15;
  }

  if (!Number.isFinite(celsius) || celsius < -273.15) {
    throw new RangeError(
      "Please enter a temperature at or above absolute zero."
    );
  }

  let converted;

  if (toUnit === "Celsius") {
    converted = celsius;
  } else if (toUnit === "Fahrenheit") {
    converted = celsius * 9 / 5 + 32;
  } else {
    converted = celsius + 273.15;
  }

  if (!Number.isFinite(converted)) {
    throw new RangeError("This temperature is too large to convert.");
  }

  return `${converted.toFixed(2)} ${symbols[toUnit]}`;
}

function showError(message) {
  errorMessage.textContent = message;
  temperatureInput.setAttribute("aria-invalid", "true");
}

function clearError() {
  errorMessage.textContent = "";
  temperatureInput.removeAttribute("aria-invalid");
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  clearError();

  const rawValue = temperatureInput.value.trim();
  const value = Number(rawValue);

  if (rawValue === "" || !Number.isFinite(value)) {
    showError("Please enter a valid numeric temperature.");
    temperatureInput.focus();
    return;
  }

  try {
    resultOutput.textContent = convertTemperature(
      value,
      fromUnitSelect.value,
      toUnitSelect.value
    );
  } catch (error) {
    showError(
      error instanceof RangeError
        ? error.message
        : "Please enter a valid numeric temperature."
    );
    temperatureInput.focus();
  }
});

resetButton.addEventListener("click", () => {
  temperatureInput.value = "";
  fromUnitSelect.value = "Celsius";
  toUnitSelect.value = "Fahrenheit";
  resultOutput.textContent = "Your converted temperature will appear here";
  clearError();
  temperatureInput.focus();
});

temperatureInput.addEventListener("input", clearError);
