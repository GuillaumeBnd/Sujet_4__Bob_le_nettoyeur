
"use strict";

let SetTorqueLimit = require('./SetTorqueLimit.js')
let SetComplianceSlope = require('./SetComplianceSlope.js')
let SetComplianceMargin = require('./SetComplianceMargin.js')
let SetCompliancePunch = require('./SetCompliancePunch.js')
let StartController = require('./StartController.js')
let SetSpeed = require('./SetSpeed.js')
let RestartController = require('./RestartController.js')
let StopController = require('./StopController.js')
let TorqueEnable = require('./TorqueEnable.js')

module.exports = {
  SetTorqueLimit: SetTorqueLimit,
  SetComplianceSlope: SetComplianceSlope,
  SetComplianceMargin: SetComplianceMargin,
  SetCompliancePunch: SetCompliancePunch,
  StartController: StartController,
  SetSpeed: SetSpeed,
  RestartController: RestartController,
  StopController: StopController,
  TorqueEnable: TorqueEnable,
};
