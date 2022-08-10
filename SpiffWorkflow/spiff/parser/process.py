from SpiffWorkflow.bpmn.parser.BpmnParser import BpmnParser
from SpiffWorkflow.bpmn.parser.BpmnParser import full_tag

from SpiffWorkflow.bpmn.specs.events import (
    StartEvent, EndEvent, IntermediateThrowEvent, BoundaryEvent, IntermediateCatchEvent, ReceiveTask, SendTask)
from SpiffWorkflow.spiff.specs import NoneTask, ManualTask, UserTask, SubWorkflowTask, TransactionSubprocess, CallActivity
from SpiffWorkflow.spiff.parser.task_spec import SpiffTaskParser, SubWorkflowParser, CallActivityParser
from SpiffWorkflow.spiff.parser.event_parsers import (SpiffStartEventParser, SpiffEndEventParser, SpiffBoundaryEventParser,
    SpiffIntermediateCatchEventParser, SpiffIntermediateThrowEventParser, SpiffSendTaskParser, SpiffReceiveTaskParser)

class SpiffBpmnParser(BpmnParser):
    OVERRIDE_PARSER_CLASSES = {
        full_tag('task'): (SpiffTaskParser, NoneTask),
        full_tag('userTask'): (SpiffTaskParser, UserTask),
        full_tag('manualTask'): (SpiffTaskParser, ManualTask),
        full_tag('subProcess'): (SubWorkflowParser, SubWorkflowTask),
        full_tag('transaction'): (SubWorkflowParser, TransactionSubprocess),
        full_tag('callActivity'): (CallActivityParser, CallActivity),
        full_tag('startEvent'): (SpiffStartEventParser, StartEvent),
        full_tag('endEvent'): (SpiffEndEventParser, EndEvent),
        full_tag('boundaryEvent'): (SpiffBoundaryEventParser, BoundaryEvent),
        full_tag('intermediateCatchEvent'): (SpiffIntermediateCatchEventParser, IntermediateCatchEvent),
        full_tag('intermediateThrowEvent'): (SpiffIntermediateThrowEventParser, IntermediateThrowEvent),
        full_tag('sendTask'): (SpiffSendTaskParser, SendTask),
        full_tag('receiveTask'): (SpiffReceiveTaskParser, ReceiveTask)
    }